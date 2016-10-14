# -*- coding: utf-8 -*-

from app import app, api
from app.api import *

api.add_resource(HelloWorld, '/api/hello')

if __name__ == '__main__':
    app.run(debug=True)