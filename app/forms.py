from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators, DateField, TimeField
#from wtforms.fields import DateField
from wtforms.validators import DataRequired



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class LookingFor(FlaskForm):
    #startdate = DateField('Начало', format='%d-%m-%Y', validators=[DataRequired(),])
    #enddate = DateField('Конец', format='%d-%m-%Y', validators=[DataRequired(),])
    startdate = DateField('Начало', format='%Y-%m-%d')
    starttime = TimeField('stt', format="%H:%M")
    enddate = DateField('Конец', format='%Y-%m-%d')
    endtime = TimeField('ent', format="%H:%M")
    submit = SubmitField('Submit')
