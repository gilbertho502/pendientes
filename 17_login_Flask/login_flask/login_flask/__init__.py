from flask import Flask
from login_flask.login_flask.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(Config)
db=SQLAlchemy(app)

from login_flask.login_flask.config import routes,models
