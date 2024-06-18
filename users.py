from flask import Blueprint, render_template
from models import db, User, Role

users_bp = Blueprint('users', __name__)

@users_bp.route('/users')
def user_list():
    users = db.session.query(User).all()
    return render_template('users_list.html', users=users)

