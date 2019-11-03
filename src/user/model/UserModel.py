from src.core.model.BaseModel import Base
from src import db
from werkzeug.exceptions import NotFound


class User(Base):
    __tablename__ = 'app_user'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(255), nullable=False)
    enabled = db.Column(db.Boolean, nullable=False)
    role = db.Column(db.String(255), nullable=False)

    @staticmethod
    def ignore_field():
        return {'password'}

    @staticmethod
    def load_by_username(username):
        user = User.query.filter_by(username=username).first()
        if user is None:
            raise NotFound
        return user
