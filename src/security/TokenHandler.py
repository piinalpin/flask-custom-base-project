from datetime import timedelta, datetime
from flask import jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, get_jti


def generate_token(identity):
    expires_delta = timedelta(days=1)
    access_token = create_access_token(identity=identity, expires_delta=expires_delta)
    expires_in = datetime.now() + expires_delta
    ret = {
        'access_token': access_token,
        'refresh_token': create_refresh_token(identity=identity, expires_delta=expires_delta),
        'expires_in': expires_in,
        'jti': get_jti(access_token)
    }
    return jsonify(ret), 200
