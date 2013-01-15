from flask import Flask
from apps import app
from apps import db
import config

app.debug = config.DEBUG
db.create_all()
app.run()