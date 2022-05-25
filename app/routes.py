from app import app
from flask import render_template, flash, redirect, url_for, session, request
from app.forms import LoginForm, LookingFor


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'fox'}
    return render_template('index.html', title='Home', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/find', methods=['GET', 'POST'])
def find():
    form = LookingFor()
    if form.validate_on_submit():
        session['startdate'] = form.startdate.data
        session['enddate'] = form.enddate.data
        session['starttime'] = str(form.starttime.data)
        session['endtime'] = str(form.endtime.data)
        return redirect(url_for('date'))
    return render_template('find.html', form=form)

@app.route('/date', methods=['GET','POST'])
def date():
    startdate = session['startdate']
    enddate = session['enddate']
    starttime = session['starttime']
    enddate = session['endtime']
    return render_template('date.html')
