from flask import Flask
from models import db
from users import users_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://server2:T3t0npack@192.168.1.28/school10'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(users_bp)

if __name__ == '__main__':
    app.run()
