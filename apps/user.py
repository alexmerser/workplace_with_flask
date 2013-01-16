from apps import app

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack

from flask.ext.login import (LoginManager, current_user, login_required,
        login_user, logout_user, UserMixin, AnonymousUser,
        confirm_login, fresh_login_required)

from apps.models import User
from apps import db

from apps.forms import SignupForm, LoginForm

@app.route('/')
def index():
    return render_template("home.html")

@app.route("/signup", methods=("GET", "POST"))
def signup():
    form = SignupForm()
    error = None
    if form.validate_on_submit():
        if form.password.data != form.password2.data:
            form.errors.update({"password" : ["passwords don't match"]})
            return render_template("signup.html", form=form)
            
        flash("Signup Success")
        user = User(form.email.data, form.password.data, form.first_name.data, form.last_name.data, form.username.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("signup.html", form=form)
    
@app.route("/login", methods=("GET", "POST"))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.login(form.email.data, form.password.data)
        if user:
            flash("Login Success")
            login_user(user, remember=True)
            return redirect("/")
        else:
            flash("Login failed")
    return render_template("login.html", form=form)

@app.route("/signout", methods=("GET",))
@login_required
def signout():
    logout_user()
    return redirect("/")
