from apps import db, site_admin
from apps.models import App, User, UserApp, UserEmail
from flask.ext.admin.contrib.sqlamodel import ModelView

site_admin.add_view(ModelView(App, db.session))
site_admin.add_view(ModelView(User, db.session))
site_admin.add_view(ModelView(UserApp, db.session))
site_admin.add_view(ModelView(UserEmail, db.session))
