from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo, ValidationError
