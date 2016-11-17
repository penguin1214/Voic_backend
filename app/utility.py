# -*- coding: utf-8 -*-

from hashlib import *
import os, time

def genToken(phone):
    token = sha1(phone+str(int(time.time()))).hexdigest()
    return token


def md5_string(s):
    return md5(s).hexdigest()