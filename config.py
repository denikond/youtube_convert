import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

app_static_dir = os.path.join("app", "static")
base_static_dir = os.path.join(basedir, "app", "static")
