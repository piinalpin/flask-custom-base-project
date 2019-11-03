from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.exceptions import NotFound

from src import app
from src.core.exception.Exception import DataNotFoundException
from src.core.util.JsonSerializer import serializer
from src.user.model.UserModel import User


@app.route('/v1/user/me', methods=['GET'])
@jwt_required
def me():
    try:
        user = User.load_by_username(get_jwt_identity())
        return serializer(user, ignore=User.ignore_field())
    except NotFound:
        return DataNotFoundException('unknown user')
