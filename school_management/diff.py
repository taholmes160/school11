from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    role = db.relationship('Role', backref=db.backref('user_list', lazy=True))  # Renamed backref
    is_active = db.Column(db.Boolean, default=True)
    is_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    profile_picture = db.Column(db.String(120))
    bio = db.Column(db.String(500))
    phone_number = db.Column(db.String(20))
    last_login_at = db.Column(db.DateTime)
    login_attempts = db.Column(db.Integer, default=0)
    password_reset_token = db.Column(db.String(120))
    password_reset_expiration = db.Column(db.DateTime)
    language = db.Column(db.String(10))
    timezone = db.Column(db.String(50))
    is_admin = db.Column(db.Boolean, default=False)
    deactivated_at = db.Column(db.DateTime)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
