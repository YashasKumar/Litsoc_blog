import os

class Config:
    SECRET_KEY = 'Hello'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'yashaskumar08@gmail.com'
    MAIL_PASSWORD = 'fungfaogacdnrarm'
    UPLOAD_FOLDER = 'new/static/media'  # Directory for media files