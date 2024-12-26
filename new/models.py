from datetime import datetime
from new import db, login_manager
from flask import current_app as app
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_seconds=1800):
        secret_key = app.config['SECRET_KEY'].encode('utf-8')  # This is already a string
        s = Serializer(secret_key, salt='my_salt')
        return s.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token):
        secret_key = app.config['SECRET_KEY']
        if isinstance(secret_key, str):
            secret_key = secret_key.encode('utf-8')  # Ensure it's bytes

        s = Serializer(secret_key, salt='my_salt')  # No expiration needed for verification
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)  # Content will store HTML from Quill
    media_filename = db.Column(db.String(120), nullable=True)  # Store filename of uploaded media
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
