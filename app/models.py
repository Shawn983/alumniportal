from . import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(100))

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    career = db.Column(db.String(100))
    contributions = db.Column(db.String(255))

class Alumni(db.Model):  # Assuming you need this for alumni-directory
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    graduation_date = db.Column(db.Date, nullable=False)
    class_number = db.Column(db.String(10))
    open_to_collaboration = db.Column(db.Boolean, default=False)
