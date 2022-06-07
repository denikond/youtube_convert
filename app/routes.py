from app import app
from flask import render_template, flash, redirect, url_for, session, request
from app.forms import LoginForm, GetLink
from config import app_static_dir, base_static_dir

from pytube import YouTube
from converter import Converter
import hashlib

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/link')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/', methods=['GET','POST'])
@app.route('/link', methods=['GET','POST'])
def link():
    form = GetLink()
    if form.validate_on_submit():
        ylink = form.data['link']
        try:
            yt = YouTube(ylink)
        except Exception as err:
            return render_template('link.html', form=form, msg="Не могу считать ссылку")
        else:
            try:
                select_stream = min(yt.streams.filter(file_extension='mp4', only_audio=True).itag_index)
            except Exception as err:
                err_msg = str(err)
                return render_template('link.html', form=form, msg=err_msg)
            else:
                stream = yt.streams.get_by_itag(select_stream)  # выбираем по тегу, в каком формате будем скачивать.
                out_filename = hashlib.md5(stream.default_filename.encode('utf-8')).hexdigest() + '.' + stream.subtype
                vobject = stream.download(output_path=base_static_dir, filename=out_filename)  # загружаем видео.
                cross = 'static/'+out_filename
                return render_template('link.html', form=form, link=cross)
    else:
        return render_template('link.html', form=form)
