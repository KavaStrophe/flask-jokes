from http import HTTPStatus
from cerberus import Validator
from flask import Blueprint, Response, jsonify, make_response, request
from jokes.services import JokeService

from routes.rest.v1.schemas import search_joke_schema

v1_jokes_bp = Blueprint('v1_jokes', __name__)
service = JokeService()


@v1_jokes_bp.route('/search', methods=["GET"])
def list_jokes() -> Response:
    v = Validator(search_joke_schema)
    if(not v.validate(request.args)):
        return make_response(jsonify({"error": v.errors}), HTTPStatus.BAD_REQUEST)
    query = request.args.get("query", "")
    data = service.search(query)
    return make_response(jsonify({"data": data}), HTTPStatus.OK)

@v1_jokes_bp.route('/<string:joke_id>', methods=["GET"])
def get_joke(joke_id: str) -> Response:
    data = service.get(joke_id)
    return make_response(jsonify({"data": data}), HTTPStatus.OK)

@v1_jokes_bp.route('/', methods=["POST"])
def create_joke() -> Response:
    content = request.get_json().get("content")
    joke = service.create(content=content)
    return make_response(jsonify({"data": joke}), HTTPStatus.OK)

@v1_jokes_bp.route('/<string:joke_id>', methods=["PUT"])
def update_joke(joke_id: str) -> Response:
    content = None
    if request.content_type == "application/json":
        content = request.get_json().get("content")
    joke = service.update(content=content, id=joke_id)
    if joke == None:
        return make_response(jsonify({"error": "Joke " + joke_id + " not found."}), HTTPStatus.NOT_FOUND)
    return make_response(jsonify({"data": joke}), HTTPStatus.OK)

@v1_jokes_bp.route('/<string:joke_id>', methods=["DELETE"])
def delete_joke(joke_id: str) -> Response:
    result = service.delete(id=joke_id)
    if not result:
        return make_response(jsonify({"error": "Joke " + joke_id + " not found."}), HTTPStatus.NOT_FOUND)
    return make_response(jsonify({"data": True}), HTTPStatus.OK)
