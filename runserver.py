from flask import Flask
from apps import app
import config

app.debug = config.DEBUG
app.run()

