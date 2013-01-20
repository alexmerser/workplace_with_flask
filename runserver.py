import config
from flask import Flask
from workplace import app, db

app.debug = config.DEBUG
if __name__ == "__main__":
    # even each runserver will call create_all(), but it won't mess things up, e.g
    # data lost, overriding, etc. For development purpose, we can keep on using this
    # it won't be used in production enviroment
    db.create_all()
    app.run()
