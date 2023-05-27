from http import HTTPStatus
from cerberus import Validator
from flask import Blueprint, Response, jsonify, make_response, request

from routes.rest.utils import extract_paging_http_request
from third_parties.jokes.chuck_norris_joke_api import ChuckNorrisJokeApi

v1_jokes_bp = Blueprint('v1_jokes', __name__)

search_schema = {
    'per_page': {
        'type': 'integer',
        'required': False,
        'min':1,
        'max':20
    },
    'page': {
        'type': 'integer',
        'required': False,
        'min':1
    },
    'query': {
        'type': 'string',
        'required': True,
        'minlength':3,
        'maxlength':120
    }
}

@v1_jokes_bp.route('/', methods=["GET"])
def list_jokes() -> Response:
    v = Validator(search_schema)
    if(not v.validate(request.args)):
        return make_response(jsonify({"error": v.errors}), HTTPStatus.BAD_REQUEST)
    paging = extract_paging_http_request(request)
    query = request.args.get("query", "")
    chuck_api = ChuckNorrisJokeApi()
    data = chuck_api.search(query, paging.per_page, paging.page)
    return make_response(jsonify({"data": data, "paging": {"page": paging.page, "per_page": paging.per_page}}), HTTPStatus.OK)

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
