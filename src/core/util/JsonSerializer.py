from flask import jsonify
from sqlalchemy.inspection import inspect


def serializer(obj, with_relationships=True, ignore=None):
    d = {}
    for column in obj.__table__.columns:
        if with_relationships and len(column.foreign_keys) > 0:
            # Skip foreign keys
            continue
        d[column.name] = getattr(obj, column.name)

    if with_relationships:
        for relationship in inspect(type(obj)).relationships:
            val = getattr(obj, relationship.key)
            d[relationship.key] = serializer(val) if val else None

    if ignore is not None:
        for value in ignore:
            del d[value]
    return jsonify(d)
