from app import app
from flask import render_template, flash, redirect, url_for, session, request
from app.forms import LoginForm, GetLink

from pytube import YouTube
from converter import Converter
import hashlib

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

@app.route('/link', methods=['GET','POST'])
def link():
    form = GetLink()
    if form.validate_on_submit():
        ylink = form.data['link']
        yt = YouTube(ylink)

        select_stream = min(yt.streams.filter(file_extension='mp4', only_audio=True).itag_index)
        stream = yt.streams.get_by_itag(select_stream)  # выбираем по тегу, в каком формате будем скачивать.
        vobject = stream.download()

        vobject = stream.download(output_path="static", filename=stream.default_filename)  # загружаем видео.
        with open(vobject, "rb") as f:
            bytes1 = f.read()  # read file as bytes
            readable_hash = hashlib.md5(bytes1).hexdigest()
            #print(readable_hash)

            return render_template('link.html', form=form)

    return render_template('link.html', form=form)
