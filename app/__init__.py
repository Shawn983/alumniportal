from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)

    with app.app_context():
        from .routes import main  # Assuming 'main' is the blueprint in routes.py
        app.register_blueprint(main)
        db.create_all()  # Creates database tables from SQLAlchemy models if they don't exist

    return app
