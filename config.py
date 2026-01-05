from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# MySQL config (XAMPP defaults: user=root, password empty)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/activity_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
