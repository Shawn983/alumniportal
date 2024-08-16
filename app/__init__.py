from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://default:kFfMWt6Zc1oX@ep-square-scene-a1p3btq7-pooler.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

#Setup console logging
if not app.debug:
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    app.logger.addHandler(stream_handler)

app.logger.setLevel(logging.INFO)
app.logger.info('Flask App startup')
    