from flask import request
from werkzeug.exceptions import UnsupportedMediaType

from functools import wraps


def validate_json_content_type(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Checking content type is in JSON format"""
        data = request.get_json(silent=True)
        if data is None:
            raise UnsupportedMediaType('Content type must be in application/json')
        return func(*args, **kwargs)
    return wrapper
