from apps import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    date_signed_up = db.Column(db.Date, nullable=False)
    date_last_login = db.Column(db.Date, nullable=True)
    date_last_activity = db.Column(db.Date, nullable=True)
    password_reset_code = db.Column(db.String(100), nullable=True)
    
    def __init__(self, email, password, first_name, last_name, username):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.date_signed_up = datetime.utcnow()

    def __repr__(self):
        return '<User %s>' % self.username

class UserEmail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.Date, nullable=False)
    verification = db.Column(db.String(200), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('email_users', lazy='dynamic'))

    def __init__(self, email, user, date_added=None):
        self.email = email
        self.user = user
        if date_added is None:
            date_added = datetime.utcnow()
        self.date_added = date_added

    def __repr__(self):
        return '<UserEmail: %s>' % self.email

class App(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(100), nullable=False)

    def __init__(self, app_name):
        self.app_name = app_name

    def __repr__(self):
        return "<App:%s>" % self.app_name

class UserApp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('app_users', lazy='dynamic'))
    app_id = db.Column(db.Integer, db.ForeignKey('app.id'))
    app = db.relationship('App', backref=db.backref('apps', lazy='dynamic'))
    
    def __init__(self, status, user, app):
        self.status = status
        self.user = user
        self.app = app

    def __repr__(self):
        return "<UserApp: %s>" % self.app.name
