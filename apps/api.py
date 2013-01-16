from apps import app
from apps import db
from apps.models import User, UserEmail, App, UserApp
import flask.ext.restless

api_manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(User, methods=['GET', 'POST', 'DELETE']) 
api_manager.create_api(UserEmail, methods=['GET', 'POST', 'DELETE'])
