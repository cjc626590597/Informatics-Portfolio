from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from website.app import app

app.config['SECRET_KEY'] = 'f8ee4cbd64785576bab7b14bc37747640c6a4837cf6cd0c5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c2096406:EUAQCKCXfeng1357@csmysql.cs.cf.ac.uk:3306/c2096406_informatic'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

csrf = CSRFProtect(app)
csrf.init_app(app)

from website import routes
from website.models import *