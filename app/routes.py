from flask import Blueprint, render_template, jsonify, request, session, redirect, url_for, current_app
import bcrypt
from .models import Event, Profile, Alumni, Newsfeed, CollaborationRequest
from datetime import datetime, timedelta
from . import db

main = Blueprint('main', __name__)
#routes for website
@main.route('/')
def home():
    current_time = datetime.now()
    one_month_ago = current_time - timedelta(days=30)
    upcoming_events = Event.query.filter(Event.event_date >= current_time).order_by(Event.event_date.asc()).all()
    newsfeed = Newsfeed.query.filter(Newsfeed.date_published >= one_month_ago).order_by(Newsfeed.date_published.desc()).all()
    return render_template('index.html', upcoming_events=upcoming_events, newsfeed=newsfeed)

@main.route('/api/profile', methods=['GET'])
def get_profile():
    if 'user_id' not in session:
        return jsonify({'status': 'error', 'message': 'User not logged in'}), 401

    user_id = session['user_id']
    user = Alumni.query.get(user_id)

    if not user:
        return jsonify({'status': 'error', 'message': 'User not found'}), 404

    profile_data = {
        'fullname': user.full_name,
        'graduationDate': user.graduation_date.strftime('%Y-%m-%d') if user.graduation_date else '',
        'classNumber': user.class_number,
        'contributions': user.contributions,
        'email': user.email,
        'openToCollaboration': user.open_to_collaboration
    }
    return jsonify(profile_data)

@main.route('/api/update-profile', methods=['POST'])
def update_profile():
    if 'user_id' not in session:
        return jsonify({'status': 'error', 'message': 'User not logged in'}), 401

    user_id = session['user_id']
    user = Alumni.query.get(user_id)

    if not user:
        return jsonify({'status': 'error', 'message': 'User not found'}), 404

    data = request.json
    user.full_name = data.get('fullname')
    user.graduation_date = datetime.strptime(data.get('graduationDate'), '%Y-%m-%d')
    user.class_number = data.get('classNumber')
    user.contributions = data.get('contributions')
    user.open_to_collaboration = data.get('openToCollaboration')

    db.session.commit()

    return jsonify({'status': 'success', 'message': 'Profile updated successfully'})

@main.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('main.register_login'))

    user_id = session['user_id']
    user = Alumni.query.get(user_id)
    requests = CollaborationRequest.query.filter_by(requested_person_email=user.email).all()
    return render_template('profile.html', user=user, requests=requests)


@main.route('/events')
def events():
    current_time = datetime.now()
    upcoming_events = Event.query.filter(Event.event_date >= current_time).order_by(Event.event_date.asc()).all()
    return render_template('events.html', events=upcoming_events, current_time=current_time)

@main.route('/alumni-directory')
def alumni_directory():
    alumni = Alumni.query.all()
    return render_template('alumni-directory.html', alumni=alumni)

@main.route('/api/alumni')
def api_alumni():
    alumni = Alumni.query.all()
    alumni_list = [{
        'id': alum.id,
        'fullName': alum.full_name,
        'class': f'{alum.graduation_date.year}/{alum.class_number}' if alum.graduation_date else 'N/A',
        'openToCollab': alum.open_to_collaboration
    } for alum in alumni]
    return jsonify(alumni_list)

@main.route('/newsfeed')
def newsfeed():
    all_news = Newsfeed.query.order_by(Newsfeed.date_published.desc()).all()
    return render_template('newsfeed.html', newsfeed=all_news)

@main.route('/register-login')
def register_login():
    return render_template('register-login.html')

@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    entered_password = data['password'].encode('utf-8')

    user = Alumni.query.filter_by(email=email).first()
    if user and bcrypt.checkpw(entered_password, user.password_hash.encode('utf-8')):
        session['user_id'] = user.id
        return jsonify({"status": "success", "message": "Login successful"})
    else:
        return jsonify({"status": "failed", "message": "Invalid email or password"})

@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    fullname = data['fullname']
    email = data['email']
    raw_password = data['password']

    user = Alumni.query.filter_by(email=email).first()
    if user:
        return jsonify({"status": "failed", "message": "Email already registered"})

    hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    new_user = Alumni(full_name=fullname, email=email, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    session['user_id'] = new_user.id
    return jsonify({"status": "success", "message": "Registration successful"})

@main.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('main.home'))

@main.route('/api/change-password', methods=['POST'])
def change_password():
    if 'user_id' not in session:
        return jsonify({'status': 'error', 'message': 'User not logged in'}), 401

    user_id = session['user_id']
    user = Alumni.query.get(user_id)

    data = request.json
    current_password = data.get('currentPassword').encode('utf-8')
    new_password = data.get('newPassword').encode('utf-8')

    if not user or not bcrypt.checkpw(current_password, user.password_hash.encode('utf-8')):
        return jsonify({'status': 'error', 'message': 'Current password is incorrect'}), 401

    user.password_hash = bcrypt.hashpw(new_password, bcrypt.gensalt()).decode('utf-8')
    db.session.commit()

    return jsonify({'status': 'success', 'message': 'Password updated successfully'})

@main.route('/submit-collab-request', methods=['POST'])
def submit_collab_request():
    data = request.get_json()
    try:
        new_request = CollaborationRequest(
            requestor_full_name=data.get('requestorName'),
            requestor_email=data.get('requestorEmail'),
            description=data.get('description'),
            requested_person_full_name=data.get('alumniName'),
            requested_person_email=data.get('alumniEmail'),
            date_of_request=datetime.now()
        )
        db.session.add(new_request)
        db.session.commit()
        return jsonify({"status": "success", "message": "Collaboration request sent"})
    except Exception as e:
        current_app.logger.error('Failed to submit collaboration request: %s', e)
        db.session.rollback()
        return jsonify({"status": "error", "message": "Failed to submit collaboration request"}), 500
