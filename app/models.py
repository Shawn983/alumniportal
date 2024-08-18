from .database import db
from datetime import datetime
#models for databases
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    event_date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(100))
    description = db.Column(db.Text)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text)

class Alumni(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    graduation_date = db.Column(db.Date)
    class_number = db.Column(db.String(100))
    contributions = db.Column(db.String(500))
    open_to_collaboration = db.Column(db.Boolean, default=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

class Newsfeed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(255), nullable=False)
    date_published = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    news_text = db.Column(db.Text, nullable=False)

class CollaborationRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    requestor_full_name = db.Column(db.String(100), nullable=False)
    requestor_contact_number = db.Column(db.String(20))
    requestor_email = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    requested_person_full_name = db.Column(db.String(100), nullable=False)
    requested_person_email = db.Column(db.String(100), nullable=False)
    date_of_request = db.Column(db.DateTime, default=datetime.utcnow)