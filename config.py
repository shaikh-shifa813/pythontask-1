#Imports Flask framework and SQLAlchemy ORM
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Creates a Flask application
app = Flask(__name__)

#MySQL config (XAMPP defaults: user=root, password empty)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/activity_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#links it to the Flask app.
db = SQLAlchemy(app)
