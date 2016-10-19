# -*- coding: utf-8 -*-

import flask_login
from flask import request, render_template, redirect, url_for
from app import app, db, login_manager
from models import *


@login_manager.user_loader
def user_loader(id):
    print id
    user = db.session.query(User).filter(id == User.id).first()
    return user


# @login_manager.request_loader
# def request_loader(request):
#     id = request.form.get('id')
#     user = db.session.query(User).filter(User.id == id).first()
#     user.is_authenticated = request.form['password'] == user.password
#
#     return user


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        data = request.form
        phone = data['phone']
        password = data['password']
        user = db.session.query(User).filter(User.phone == phone).first()
        if user:
            if user.password == password:
                flask_login.login_user(user)
                return redirect(url_for('protected'))
        else:
            return 'error'


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as : ' + str(flask_login.current_user.id)


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

