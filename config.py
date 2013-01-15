# configuration
import os
ROOT = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

DATABASE = 'dev.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(ROOT, DATABASE)

USERNAME = 'admin'
PASSWORD = 'default'

DEBUG_TB_INTERCEPT_REDIRECTS = False
DEBUG = True