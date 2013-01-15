from apps import app

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack

from flask.ext.wtf import Form, TextField, Required

class LoginForm(Form):
    email = TextField("email", validators = [Required()])

@app.route("/login", methods=("GET", "POST"))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Success")
        return redirect("/")
    return render_template("login.html", form=form)
    
