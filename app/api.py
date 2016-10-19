# -*- coding: utf-8 -*-

import flask_login, json
from flask_restful import Resource, reqparse
from flask import request
from app import api
from models import User


parser = reqparse.RequestParser()


# def request_parser():
#     parser.add_argument('data', action='append')
#     return parser.parse_args()['data'][0]


# class ApiLogin(Resource):
#     def post(self):
#         data = request.form
#         email = data['email']
#         if data['pwd'] == users[email]['pwd']:
#             user = User()
#             user.id = email
#             flask_login.login_user(user)
#             return 'login success'
#
#         return 'Bad login'
#
#
# class ApiProtected(Resource):
#     @flask_login.login_required
#     def get(self):
#         return 'Logged in as: ' + flask_login.current_user.id
#
#
# api.add_resource(ApiLogin, '/api/login')
# api.add_resource(ApiProtected, '/protected')
