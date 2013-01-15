from apps import app

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack

from flask.ext.wtf import Form, TextField, Required,  \
    PasswordField
from apps.models import User
from apps import db

class SignupForm(Form):
    email = TextField("Email", validators = [Required()])
    password = PasswordField("password", validators = [Required()])
    password2 = PasswordField("password2", validators = [Required()])
    first_name = TextField("First Name", validators = [Required()])
    last_name = TextField("Last Name", validators = [Required()])
    username = TextField("User Name", validators = [Required()])

class SigninForm(Form):
    email = TextField("Email", validators = [Required()])
    password = PasswordField("password", validators = [Required()])

@app.route("/signup", methods=("GET", "POST"))
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash("Signup Success")
        user = User(form.email.data, form.password.data, form.first_name.data, form.last_name.data, form.username.data)
        db.session.add(user)
        db.session.commit()
        return redirect("/")
    return render_template("signup.html", form=form)
    
@app.route("/signin", methods=("GET", "POST"))
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        flash("Signin Success")
        can_login = User.can_signin(form.email.data, form.password.data)
        if can_login:
            return redirect("/")
    return render_template("signin.html", form=form)

@app.route("/signout", methods=("GET"))
def signout():
    return redirect("/")
