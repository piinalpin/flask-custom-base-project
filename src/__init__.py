from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from src.core.config.DatabaseConfig_ import DatabaseConfig


# Define App
app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'HS256'
app.config["JSON_SORT_KEYS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = DatabaseConfig().get_connection()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

CORS(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)

from .user.model.UserModel import User
migrate = Migrate(app, db)

from src.core.controller.Main import *
from src.core.exception.ApiErrorHandler import *
from src.user.controller.UserController import *

