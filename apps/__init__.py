from flask import Flask
app = Flask(__name__)

import apps.archive
import apps.news
import apps.todolist
import apps.user
