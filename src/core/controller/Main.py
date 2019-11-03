from flask import jsonify, request
from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity
from werkzeug.exceptions import BadRequest, NotFound

from src import app
from src.core.exception.Exception import InvalidGrant
from src.core.util.PasswordGenerator import verify_password
from src.security.BasicAuthorization import login_required
from src.security.TokenHandler import generate_token
from src.user.model.UserModel import User


@app.route('/', methods=['GET'])
def main():
    return jsonify({'message': 'ok'})


@app.route('/oauth/token', methods=['POST'])
@login_required
def oauth():
    try:
        username = None if request.form['username'] is None else request.form['username']
        password = None if request.form['password'] is None else request.form['password']
        user = User.load_by_username(username)
        if not verify_password(user.password, password):
            raise BadRequest
    except BadRequest:
        return InvalidGrant()
    except NotFound:
        return InvalidGrant()
    return generate_token(user.username)


@app.route('/oauth/token/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh_token():
    return generate_token(get_jwt_identity())
