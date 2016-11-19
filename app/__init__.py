# -*- coding: utf-8 -*-

#initialization
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import flask_login
import config

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = "yangjinglei"

api = Api(app)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app, use_native_unicode="utf8")
# import models
# db.create_all()

from app import views
