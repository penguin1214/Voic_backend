# -*- coding: utf-8 -*-

from app import app, api
from app.api import *


if __name__ == '__main__':
    app.run(debug=True)