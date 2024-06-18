from flask import Blueprint, render_template
from school_management.models import db, User, Role

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/')
def home():
    return render_template('home.html')

@users_bp.route('/list')
def user_list():
    users = db.session.query(User).all()
    return render_template('users_list.html', users=users)

