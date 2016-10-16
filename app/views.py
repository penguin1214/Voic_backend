# -*- coding: utf-8 -*-

from flask import render_template, url_for
from app import app, db, login_manager

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')
