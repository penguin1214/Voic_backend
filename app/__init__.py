# -*- coding: utf-8 -*-

#initialization
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config.from_object("config")
api = Api(app)
db = SQLAlchemy(app, use_native_unicode="utf8")

from app import views
