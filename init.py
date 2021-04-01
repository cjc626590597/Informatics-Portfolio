from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder="static")
app.config['SECRET_KEY'] = 'f8ee4cbd64785576bab7b14bc37747640c6a4837cf6cd0c5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c2096406:EUAQCKCXfeng1357@csmysql.cs.cf.ac.uk:3306/c2096406_informatic'

db = SQLAlchemy(app,session_options={"autoflush": False, "autocommit": False})

login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view= 'users.login'

