import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret-key')  # Use environment variable
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:////tmp/database.db')  # Read DB URI from env
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')  # Read email from env
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')  # Read password from env

    UPLOAD_FOLDER = 'new/static/media'