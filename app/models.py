# -*- coding: utf-8 -*-
from app import login_manager, db
from utility import *
import flask_login, json


class User(flask_login.UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(12), unique=True)
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

    def __init__(self,phone,auth_token='',voice_id=''):
        self.phone = phone
        self.auth_token = auth_token
        self.voice_id = 'oiwrj' + phone

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    title = db.Column(db.String(20))
    img_res_string = db.Column(db.String(20))
    current_stat = db.Column(db.Integer)
    color_stat_pair = db.Column(db.String(150))

    def __init__(self, user_id, title, img_res_string, current_stat, color_stat_pair):
        self.user_id = user_id
        self.title = title
        self.img_res_string = img_res_string
        self.current_stat = current_stat
        self.color_stat_pair = json.dumps(color_stat_pair)



