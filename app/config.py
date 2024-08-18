import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://alumni_management_db_user:0pRGnQMGN7vwNh8EeXe9ZkVRYmUbC9b1@dpg-cr10bs3tq21c73cmmvq0-a.singapore-postgres.render.com/alumni_management_db')
    SECRET_KEY = os.getenv('SECRET_KEY') or os.urandom(24)
    
    