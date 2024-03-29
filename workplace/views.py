from datetime import datetime
from flask import (Flask, request, session, g, redirect, url_for, abort,
    render_template, flash, _app_ctx_stack)
from flask.ext.login import (LoginManager, current_user, login_required,
    login_user, logout_user, UserMixin, AnonymousUser,
    confirm_login, fresh_login_required)
from workplace import app
from workplace.forms import (AccountGeneralForm, AccountEmailsForm, AccountListsForm, 
    AccountPasswordForm, AccountProfileForm, LoginForm, RegisterForm, ResetPasswordForm)
from workplace.models import db, User


#workplace applications
@app.route('/workplace/')
@app.route('/workplace')
@app.route('/')
def workplace():
    return render_template("workplace.html", title="Personal apps made for the connected world.")

@app.route('/archive/')
@app.route('/archive')
def archive():
    return render_template("archive.html", title="Archive")

@app.route('/news/')
@app.route('/news')
def news():
    return render_template("news.html", title="News")

@app.route('/todo/')
@app.route('/todo')
def todo():
    return render_template("todo.html", title="To-Do List")

#workplace pages
@app.route("/register/", methods=("GET", "POST"))
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
    
@app.route("/login/", methods=("GET", "POST"))
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
@app.route("/hlogin/", methods=("GET", "POST"))
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


@app.route("/logout/", methods=("GET",))
@app.route("/logout", methods=("GET",))
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route("/reset_password/", methods=("GET", "POST"))
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

@app.route("/profile/")
@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html", title="Profile")

@app.route("/messages/<int:message_id>")
@app.route("/messages/")
@app.route("/messages")
@login_required
def messages(message_id=None):
    return render_template("messages.html", title="Messages")

@app.route("/notifications/")
@app.route("/notifications")
@login_required
def notifications():
    return render_template("notifications.html", title="Notifications")

#Account Pages
@app.route("/a/general/", methods=("GET", "POST"))
@app.route("/a/general", methods=("GET", "POST"))
@login_required
def a_general():
    form = AccountGeneralForm()
    return render_template("a_general.html", form=form, title="Account - General")

@app.route("/a/applications/", methods=("GET", "POST"))
@app.route("/a/applications", methods=("GET", "POST"))
@login_required
def a_applications():
    return render_template("a_applications.html", title="Account/Applications")

#Insert info to UserApp Model
@app.route("/a/applications/add/<application_name>")
@login_required
def a_applications_add():
    pass

#Removes all content
#Update UserApp Model status for 'inactive', count down for 2 weeks.
@app.route("/a/applications/remove/<application_name>")
@login_required
def a_applications_remove():
    pass

#Cancels removal
#Update UserApp Model status
@app.route("/a/applications/cancel_removal/<application_name>")
@login_required
def a_applications_cancel_removal():
    pass

@app.route("/a/emails/", methods=("GET", "POST"))
@app.route("/a/emails", methods=("GET", "POST"))
@login_required
def a_emails():
    form = AccountEmailsForm()
    return render_template("a_emails.html", form=form, title="Account/Emails")

@app.route("/a/lists/", methods=("GET", "POST"))
@app.route("/a/lists", methods=("GET", "POST"))
@login_required
def a_lists():
    form = AccountListsForm()
    return render_template("a_lists.html", form=form, title="Account/Password")

@app.route("/a/password/", methods=("GET", "POST"))
@app.route("/a/password", methods=("GET", "POST"))
@login_required
def a_password():
    form = AccountPasswordForm()
    return render_template("a_password.html", form=form, title="Account/Password")

@app.route("/a/profile/", methods=("GET", "POST"))
@app.route("/a/profile", methods=("GET", "POST"))
@login_required
def a_profile():
    form = AccountProfileForm()
    return render_template("a_profile.html", form=form, title="Account/Profile")

# What's this page for?

@app.route("/succ/")
@app.route("/succ")
def succ():
    return render_template("succ.html")
