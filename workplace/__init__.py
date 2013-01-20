import config
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.sqlalchemy import SQLAlchemy

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
from workplace.models import Anonymous
login_manager.anonymous_user = Anonymous
login_manager.login_view = "login"
login_manager.login_message = u"Please log in to access this page."
login_manager.refresh_view = "reauth"

from workplace.models import User

@login_manager.user_loader
def load_user(id):
    return User.get_user(id)

#Admin
from flask.ext.admin import Admin
site_admin = Admin(app)

import workplace.views
import workplace.models
import workplace.admin

# RESTful APIs
if config.REST_API_ENABLED:
    import workplace.api
