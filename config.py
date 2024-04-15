import os

from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():

  FLASK_APP = os.getenv('FLASK_APP')
  FLASK_ENV = os.getenv('FLASK_ENV')
  SECRET_KEY = os.environ.get('WHY_ALL_CAPS_THO') or "I will never forget to use an R statement again"
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_NOTIFICATIONS = False