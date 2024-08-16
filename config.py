import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('Database_URL', 'postgresql://default:kFfMWt6Zc1oX@ep-square-scene-a1p3btq7-pooler.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
    
    