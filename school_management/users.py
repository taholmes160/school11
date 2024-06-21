from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from werkzeug.security import check_password_hash
from school_management.models import db, User
from school_management.forms import LoginForm

users_bp = Blueprint('users', __name__, url_prefix='/users')

# Initialize the LoginManager object
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    print(f"Loading user with ID: {user_id}")
    return User.query.get(int(user_id))

@users_bp.route('/')
def home():
    return render_template('home.html')

@users_bp.route('/list')
@login_required
def user_list():
    print("Entered user_list route")
    if not check_access_student_list():
        users = User.query.all()
        return render_template('users/users_list.html', users=users)
    else:
        abort(403)

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        print("User is already authenticated, redirecting to user_list")
        return redirect(url_for('users.user_list'))

    form = LoginForm()
    if form.validate_on_submit():
        print(f"Form submitted with username: {form.username.data}")
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            print(f"User found: {user.username}")
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user, remember=True)
                print(f"User logged in: {user.username}")
                next_page = request.args.get('next')
                print(f"Next page: {next_page}")
                return redirect(next_page or url_for('users.user_list'))
            else:
                print("Invalid password")
                flash('Invalid username or password', 'error')
        else:
            print("User not found")
            flash('Invalid username or password', 'error')

    return render_template('users/login.html', form=form)

@users_bp.route('/logout')
@login_required
def logout():
    print(f"User logging out: {current_user.username}")
    logout_user()
    return redirect(url_for('users.login'))

def check_access_student_list():
    if current_user.is_authenticated:
        print(f"Checking access for user: {current_user.username}")
        user_roles = [current_user.role_id]  # Assuming role_id is directly in User
        restricted_roles = [15, 17, 19, 20]  # List of restricted role IDs
        if any(role_id in user_roles for role_id in restricted_roles):
            print(f"Access denied for user: {current_user.username} with roles {user_roles}")
            return True
        else:
            print(f"Access granted for user: {current_user.username} with roles {user_roles}")
    return False
