from flask import Flask, redirect, url_for
from school_management.models import db
from school_management.users import users_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://server2:T3t0npack@192.168.1.28/school10'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(users_bp)

@app.route('/')
def index():
    return redirect(url_for('users.home'))

if __name__ == '__main__':
    app.run(debug=True)



