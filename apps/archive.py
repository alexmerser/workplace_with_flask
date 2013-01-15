from apps import app

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack

@app.route('/')
def index():
    return redirect(url_for("signup"))
