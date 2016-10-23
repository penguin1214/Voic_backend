# -*- coding: utf-8 -*-
from app import login_manager, db
import flask_login


class User(flask_login.UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(12), unique=True)
    password = db.Column(db.String(50))
    voice_id = db.Column(db.String(100), unique=True)
    auth_token = db.Column(db.String(150), unique=True)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __init__(self,phone,password,auth_token='',voice_id=''):
        self.phone = phone
        self.password = password
        self.auth_token = auth_token
        self.voice_id = voice_id


