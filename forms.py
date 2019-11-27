'''To handle the web forms in this application I'm going to use the Flask-WTF extension,
   which is a thin wrapper around the WTForms package that nicely integrates it with Flask.
   Flask extensions are regular Python packages that are installed with pip. You can go ahead and
   install Flask-WTF in your virtual environment:
    (venv) $ pip install flask-wtf'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class addinfo(FlaskForm):
    username=StringField('Username')
    password = PasswordField('Password')
    email=StringField('Email')
    phoneno=StringField('Phone Number')
    submit = SubmitField('Add')

class searchinfo(FlaskForm):
    username=StringField('Username')
    submit=SubmitField('Search')