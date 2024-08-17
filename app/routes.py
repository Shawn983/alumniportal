from flask import Blueprint, render_template
from .models import Event, Profile  # Make sure these are your actual model names
from . import db  # Only if needed directly, not typically required if using models
from .models import Alumni
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/profile/<int:profile_id>')
def profile(profile_id):
    person = Profile.query.get_or_404(profile_id)
    return render_template('profile.html', person=person)

@main.route('/events')
def events():
    events = Event.query.all()
    return render_template('events.html', events=events)

@main.route('/alumni-directory')
def alumni_directory():
    alumni = Alumni.query.all()  # Assuming you have an Alumni model defined
    return render_template('alumni-directory.html', alumni=alumni)
