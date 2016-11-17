# -*- coding: utf-8 -*-

from app import app, api, socketio
from app.api import *
from time import ctime



if __name__ == '__main__':
    # app.run(debug=True)
    socketio.run(app)