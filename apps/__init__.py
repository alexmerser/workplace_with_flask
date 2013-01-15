from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# debug toolbar
toolbar = DebugToolbarExtension(app)

#SQLAlchemy
db = SQLAlchemy(app)

#Login
from flask.ext.login import LoginManager
login_manager = LoginManager()
login_manager.setup_app(app)

#Admin
from flask.ext.admin import Admin
site_admin = Admin(app)


import apps.archive
import apps.news
import apps.todolist
import apps.user
import apps.models
import apps.admin
