from flask import Response, jsonify
from Book_Library_App import app, db


class ErrorResponse:
    """"Class to errors handling"""
    def __init__(self, message: str, http_status: int):
        self.payload = {
            'success': False,
            'message': message
        }
        self.http_status = http_status

    def to_response(self) -> Response:
        """Return RESPONSE object"""
        response = jsonify(self.payload)
        response.status_code = self.http_status
        return response


@app.errorhandler(404)
def not_found_error(err):
    return ErrorResponse(err.description, 404).to_response()


@app.errorhandler(400)
def bad_request_error(err):
    messages = err.data.get('messages', {}).get('json', {})
    return ErrorResponse(messages, 400).to_response()


@app.errorhandler(415)
def unsupported_media_error(err):
    """Check Media type errors"""
    return ErrorResponse(err.description, 415).to_response()


@app.errorhandler(500)
def internal_serval_error(err):
    """Check QUERY to database"""
    db.session.rollback()
    return ErrorResponse(err.description, 500).to_response()
