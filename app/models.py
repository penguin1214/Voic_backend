# -*- coding: utf-8 -*-
import flask_login
from app import login_manager


users = {'foo@bar.tld': {'pwd': 'secret'}}


class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    user.is_authenticated = request.form['pwd'] == users[email]['pw']

    return user
