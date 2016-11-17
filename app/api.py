# -*- coding: utf-8 -*-

import flask_login, json, hashlib
from flask_restful import Resource, reqparse
from flask import request
from app import api, db
from models import User, Device
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
        user = User(phone)
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
        _user = db.session.query(User).filter(User.phone == phone).first()

        if _user:
            _id = _user.id
            auth_token = genToken(phone)
            _user.auth_token = auth_token
            db.session.commit()
            ret["user_id"] = _id
            ret["auth_token"] = auth_token
            return response_packer(0, "success", ret)

        else:
            return response_packer(1, "用户不存在", ret)


# class ApiLogout(Resource):


class ApiAddDevice(Resource):
    """
    每次添加设备时都通知服务器，服务器返回设备的id，便于退出时刷新。
    """
    def post(self):
        ret = {}
        data = request.get_json()["data"]
        user_id = request.get_json()["userId"]
        title = data["title"]
        img_res_string = data["img_res_string"]
        current_stat = data["current_stat"]
        color_stat_pair = data["color_stat_pair"]
        device = Device(user_id, title, img_res_string, current_stat, color_stat_pair)
        db.session.add(device)
        db.flush()
        # 是否可以获取设备id
        device_id = device.id
        db.session.commit()

        ret["device_id"] = device_id
        return response_packer(0, "success", ret)


class ApiRefreshDeviceInfo(Resource):
    """
    设备信息发生改变时，刷新。
    """
    def post(self):
        ret = {}
        data = request.get_json()["data"]
        user_id = data["user_id"]
        color_stat_pair = data["color_stat_pair"]


api.add_resource(ApiRegister, '/api/user/register')
api.add_resource(ApiLogin, '/api/user/login')
api.add_resource(ApiAddDevice, '/api/device/add')
api.add_resource(ApiRefreshDeviceInfo, '/api/device/refresh')
