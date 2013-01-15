from flask.ext.admin.contrib.sqlamodel import ModelView
from apps.models import User, UserEmail, App, UserApp
from apps import site_admin
from apps import db

site_admin.add_view(ModelView(User, db.session))
site_admin.add_view(ModelView(UserEmail, db.session))
site_admin.add_view(ModelView(App, db.session))
site_admin.add_view(ModelView(UserApp, db.session))
