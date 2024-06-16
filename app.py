from flask import Flask
from models import db, User, Role

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<username>:<password>@<host>/<database_name>'
db.init_app(app)

@app.route('/')
def index():
    users = User.query.all()
    return 'Hello, {} users!'.format(len(users))

if __name__ == '__main__':
    app.run()
