from flask import Blueprint, render_template
from models import User

users_bp = Blueprint('users', __name__)

@users_bp.route('/users')
def user_list():
    users = User.query.all()
    return render_template('user_list.html', users=users)
