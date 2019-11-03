from flask_jwt_extended import exceptions
from src import app, jwt
from src.core.exception.Exception import Unauthorized, TokenErrorException


@app.errorhandler(exceptions.NoAuthorizationError)
def no_authorization_error(e):
    return Unauthorized()


@jwt.invalid_token_loader
def invalid_token_handler(e):
    return TokenErrorException('Invalid Token')


@jwt.expired_token_loader
def expired_token_handler(e):
    return TokenErrorException('Token Expired')
