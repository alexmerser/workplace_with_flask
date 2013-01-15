from flask import Flask
from apps import app


app.debug = config.DEBUG


app.run()

