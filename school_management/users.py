from flask import Blueprint, render_template, redirect, url_for, flash, abort
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.security import check_password_hash
from school_management.models import db, User
from school_management.forms import LoginForm

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/')
def home():
    return render_template('home.html')

@users_bp.route('/list')
@login_required
def user_list():
    if not check_access_student_list():
        users = User.query.all()
        return render_template('users/users_list.html', users=users)
    else:
        abort(403)

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.user_list'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('users.user_list'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('users/login.html', form=form)

@users_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))

def check_access_student_list():
    if current_user.is_authenticated:
        user_roles = [role.id for role in current_user.roles]
        restricted_roles = [15, 17, 19, 20]  # List of restricted role IDs
        if any(role_id in user_roles for role_id in restricted_roles):
            return True
    return False
