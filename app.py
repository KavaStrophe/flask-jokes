from http import HTTPStatus
from flask import Response, jsonify, make_response

from lib.app import app
from routes.rest.v1.jokes import v1_jokes_bp

app.register_blueprint(v1_jokes_bp, url_prefix='/api/v1/jokes')

@app.errorhandler(404)
def handle_not_found_error(error) -> Response:
    print(error)
    return make_response(jsonify({'error': 'Not Found'}), HTTPStatus.NOT_FOUND)

@app.errorhandler(Exception)
def handle_generic_error(error) -> Response:
    print(error)
    return make_response(jsonify({'error': 'Internal Server Error'}), HTTPStatus.INTERNAL_SERVER_ERROR)
