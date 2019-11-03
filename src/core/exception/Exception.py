from datetime import datetime

from flask import jsonify, request
from flask_api import status


def NOW():
    return datetime.now()


def construct_data(message, status, data=None, error=None):
    if data is None:
        data = dict()
    data['error'] = error
    data['status'] = status
    data['message'] = message
    data['timestamp'] = NOW()
    data['path'] = request.path
    data['errors'] = None
    return data


def DataNotFoundException(message):
    return jsonify(construct_data(message, status=status.HTTP_404_NOT_FOUND, error='Not Found')), \
           status.HTTP_404_NOT_FOUND


def DuplicateDataException(message):
    return jsonify(construct_data(message, status=status.HTTP_400_BAD_REQUEST, error='Bad Request')), \
           status.HTTP_400_BAD_REQUEST


def InvalidGrant():
    data = dict()
    data['error'] = 'invalid_grant'
    data['error_description'] = 'Bad Credentials'
    return jsonify(data), status.HTTP_400_BAD_REQUEST


def Unauthorized():
    return jsonify(construct_data('Bad credentials', status=status.HTTP_401_UNAUTHORIZED, error='Unauthorized')), \
           status.HTTP_401_UNAUTHORIZED


def TokenErrorException(message):
    return jsonify(construct_data(message, status=status.HTTP_401_UNAUTHORIZED, error='Unauthorized')), \
           status.HTTP_401_UNAUTHORIZED
