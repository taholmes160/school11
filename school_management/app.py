from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_session import Session
from school_management.models import db
from school_management.users import users_bp, login_manager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://server2:T3t0npack@192.168.1.28/school10'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure session to use filesystem (instead of signed cookies)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_KEY_PREFIX'] = 'myapp_session:'
Session(app)

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'users.login'
login_manager.refresh_view = 'users.login'
login_manager.needs_refresh_message = (u"Session timed out, please re-login")
login_manager.needs_refresh_message_category = "info"

app.register_blueprint(users_bp)

@app.route('/')
def index():
    return redirect(url_for('users.home'))

@app.route('/debug-session')
def debug_session():
    try:
        is_authenticated = current_user.is_authenticated
        user_id = current_user.get_id()
        print(f"Current user authenticated: {is_authenticated}")
        print(f"Current user id: {user_id}")
        return f"Session Debug - Authenticated: {is_authenticated}, User ID: {user_id}"
    except Exception as e:
        print(f"Error in debug_session: {e}")
        return f"Error in debug_session: {e}"

if __name__ == '__main__':
    app.run(debug=True)
