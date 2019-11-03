from src import db


class Base(db.Model):
    __abstract__ = True

    created_at = db.Column(db.TIMESTAMP, default=db.func.now(), nullable=False)
    created_by = db.Column(db.Integer, nullable=False)
    deleted_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP, default=db.func.now(), onupdate=db.func.now())
