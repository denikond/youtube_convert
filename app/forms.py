from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators, DateField, TimeField
#from wtforms.fields import DateField
from wtforms.validators import DataRequired



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class GetLink(FlaskForm):
    link = StringField('Enter Youtube Link', validators=[DataRequired()])
    submit = SubmitField('Sign In')
