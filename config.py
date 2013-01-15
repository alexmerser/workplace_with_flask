# configuration
import os
ROOT = os.path.abspath(os.path.dirname(__file__))
DATABASE = 'dev.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
SQLALCHEMY_DATABASE_URI = "sqlite:///%s/dev.db" % ROOT
