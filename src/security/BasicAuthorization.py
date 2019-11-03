from flask import request
from functools import wraps
from src.core.exception.Exception import Unauthorized
import base64


def check(authorization_header):
    username = 'hyuga'
    password = 'hinata'
    encode = authorization_header.split()[-1]
    basic = base64.b64encode((username + ":" + password).encode('ascii')).decode('ascii')
    if encode == basic:
        return True


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        authorization_header = request.headers.get('Authorization')
        if authorization_header and check(authorization_header):
            return f(*args, **kwargs)
        else:
            return Unauthorized()
    return decorated
