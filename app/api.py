# -*- coding: utf-8 -*-

import flask_login, json, hashlib
from flask_restful import Resource, reqparse
from flask import request
from app import api, db
from models import User
from utility import *


parser = reqparse.RequestParser()


def response_packer(result, message, data = "none"):
    return {
        "result": result,
        "message": message,
        "data": data
    }


def request_parser():
    parser.add_argument('data', action='append')
    return parser.parse_args()['data'][0]


class ApiRegister(Resource):
    def post(self):
        ret = {}
        data = request.get_json()["data"]
        phone = data["phone"]
        password = data["password"]
        user = User(phone,password)
        db.session.add(user)
        db.session.commit()

        return response_packer(0, "success", ret)


class ApiLogin(Resource):
    """
    每次登录时都生成新token，传回移动端，移动端每次请求带上token。
    """
    def post(self):
        ret = {}
        data = request.get_json()["data"]
        phone = data["phone"]
        password = data["password"]
        _user = db.session.query(User).filter(User.phone == phone).first()

        if _user:
            _pass = _user.password
            _id = _user.id
            if _pass == password:
                auth_token = genToken(phone, password)
                _user.auth_token = auth_token
                db.session.commit()
                ret["user_id"] = _id
                ret["auth_token"] = auth_token
                return response_packer(0, "success", ret)
            else:
                return response_packer(1, "密码错误", ret)
        else:
            return response_packer(1, "用户不存在", ret)

api.add_resource(ApiRegister, '/api/user/register')
api.add_resource(ApiLogin, '/api/user/login')
