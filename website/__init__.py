import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder="static")
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c2097255:Database2021@csmysql.cs.cf.ac.uk:3306/c2097255_informatics'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from website import routes