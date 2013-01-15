from flask import Flask
from apps import app
from apps import db
import config

app.debug = config.DEBUG
<<<<<<< HEAD
db.create_all()
app.run()
=======
db.create_all() #why is it creating a database everytime we run the server?
app.run()

>>>>>>> 00f2d9ad81a0da786af7c7ddadc52f8925d90577
