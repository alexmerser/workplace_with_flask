from flask import Flask
from apps import app
from apps import db
import config

app.debug = config.DEBUG
#db.create_all() #why is it creating a database everytime we run the server?
if __name__ == "__main__":
    app.run()
