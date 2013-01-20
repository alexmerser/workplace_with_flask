from apps import app

from flask import (Flask, request, session, g, redirect, url_for, abort,
    render_template, flash, _app_ctx_stack)

from flask.ext.login import (LoginManager, current_user, login_required,
    login_user, logout_user, UserMixin, AnonymousUser,
    confirm_login, fresh_login_required)

from apps.models import User
from apps import db

from apps.forms import RegisterForm, LoginForm, ResetPasswordForm

from datetime import datetime


@app.route('/')
def index():
    return render_template("home.html", title="Home Page")

@app.route("/register", methods=("GET", "POST"))
def register():
    form = RegisterForm()
    error = None
    has_error = False
    if form.validate_on_submit():
        if form.password.data != form.password2.data:
            form.errors.update({"password" : ["Passwords don't match"]})
            has_error = True
        if form.email.data != form.email2.data:
            form.errors.update({"email" : ["Emails don't match"]})
            has_error = True
        if has_error:
            return render_template("register.html", form=form, title="Register")
            
        flash("Welcome to Workplace! You were successfully registered.")
        user = User(form.email.data, form.password.data, form.first_name.data, form.last_name.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html", form=form, title="Register")
    
@app.route("/login", methods=("GET", "POST"))
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.login(form.email.data, form.password.data)
        if user:
            flash("Login Success")
            login_user(user, remember=True)
            user.date_last_login = datetime.utcnow()
            db.session.add(user)
            db.session.commit()
            return redirect("/")
        else:
            flash("Login failed")
    return render_template("login.html", form=form, title="Log In")

# login via header form
@app.route("/hlogin", methods=("GET", "POST"))
def hlogin():
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        user = User.login(form.email.data, form.password.data)
        if user:
            flash("Login Success")
            login_user(user, remember=True)
            user.date_last_login = datetime.utcnow()
            db.session.add(user)
            db.session.commit()
            return redirect("/")
        else:
            flash("Login failed")
    return render_template("login.html", form=form, title="Log In")


@app.route("/logout", methods=("GET",))
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route("/reset_password", methods=("GET", "POST"))
def reset_password():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        email = form.email.data
        if User.is_signed_email(email):
            # send a reset_password email
            flash("Your password has been reset. Create a new password by following the instructions sent to your email.")
            return redirect(url_for("succ"))
        else:
            flash("The email doesn't exist.")
    return render_template("reset_password.html", form=form, title="Forgot Pasword?")

@app.route("/succ", methods=("GET", ))
def succ():
    return render_template("succ.html")


@app.route("/profile", methods=("GET", ))
@login_required
def profile():
    return render_template("profile.html", title="Profile")

@app.route("/settings", methods=("GET", ))
@login_required
def settings():
    return render_template("settings.html", title="Settings")

@app.route("/messages", methods=("GET", ))
@login_required
def messages():
    return render_template("messages.html", title="Messages")



@app.route("/notifications", methods=("GET", ))
@login_required
def notifications():
    return render_template("notifications.html", title="Notifications")


