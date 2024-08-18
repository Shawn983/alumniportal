from flask import Flask
from .database import db
from .routes import main
from .config import Config  # Import Config

def create_app():
    app = Flask(__name__,template_folder='templates', static_folder='./static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://default:kFfMWt6Zc1oX@ep-square-scene-a1p3btq7-pooler.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require'  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Load configuration from config.py
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()  # Create database tables for our data models

    app.register_blueprint(main)
    return app
