# -*- coding: utf-8 -*-

from hashlib import *
import os, time

def genToken(phone, password):
    token = sha1(phone+password+str(int(time.time()))).hexdigest()
    return token


def md5_string(s):
    return md5(s).hexdigest()