from http import HTTPStatus

from flask import Blueprint, Response, jsonify, make_response

v1_jokes_bp = Blueprint('v1_jokes', __name__)


@v1_jokes_bp.route('/', methods=["GET"])
def list_jokes() -> Response:
    return make_response(jsonify({"data": [], "paging": {"page": 0, "per_page": 20}}), HTTPStatus.OK)

@v1_jokes_bp.route('/', methods=["POST"])
def create_joke() -> Response:
    return make_response(jsonify({"data": {}}), HTTPStatus.OK)

@v1_jokes_bp.route('/<int:joke_id>', methods=["GET"])
def get_joke(joke_id: int) -> Response:
    return make_response(jsonify({"data": {}}), HTTPStatus.OK)

@v1_jokes_bp.route('/<int:joke_id>', methods=["PUT"])
def update_joke(joke_id: int) -> Response:
    return make_response(jsonify({"data": {}}), HTTPStatus.OK)

@v1_jokes_bp.route('/<int:joke_id>', methods=["DELETE"])
def delete_joke(joke_id: int) -> Response:
    return make_response(jsonify({"data": True}), HTTPStatus.OK)
