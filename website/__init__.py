from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder="static")
app.config['SECRET_KEY'] = 'f8ee4cbd64785576bab7b14bc37747640c6a4837cf6cd0c5'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c2096406:EUAQCKCXfeng1357@csmysql.cs.cf.ac.uk:3306/informatics'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:a123456@127.0.0.1:3306/group_user'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from website import routes