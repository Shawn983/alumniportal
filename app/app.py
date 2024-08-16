from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock database
alumni = [
    {'id': 1, 'name': 'John Doe', 'email': 'john.doe@example.com', 'career': 'Software Engineer', 'contributions': 'Speaker at 2020 Alumni Event'},
    {'id': 2, 'name': 'Jane Smith', 'email': 'jane.smith@example.com', 'career': 'Data Scientist', 'contributions': 'Donated $500 in 2021'}
]

events = [
    {'title': 'Annual Alumni Meetup 2024', 'date': '2024-09-15', 'location': 'Alumni Hall'},
    {'title': 'Fundraising Gala 2024', 'date': '2024-11-20', 'location': 'Central Hotel Ballroom'}
]

@app.route('/')
def index():
    return render_template('index.html', alumni=alumni)

@app.route('/profile/<int:alumni_id>')
def profile(alumni_id):
    person = next((item for item in alumni if item["id"] == alumni_id), None)
    return render_template('profile.html', person=person)

@app.route('/events')
def list_events():
    return render_template('events.html', events=events)

@app.route('/update_profile/<int:alumni_id>', methods=['POST'])
def update_profile(alumni_id):
    for person in alumni:
        if person['id'] == alumni_id:
            person['name'] = request.form['name']
            person['email'] = request.form['email']
            person['career'] = request.form['career']
            person['contributions'] = request.form['contributions']
            break
    return redirect(url_for('profile', alumni_id=alumni_id))

if __name__ == '__main__':
    app.run(debug=True, port=1234)
