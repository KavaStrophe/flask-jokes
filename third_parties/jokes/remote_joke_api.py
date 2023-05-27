from third_parties.jokes.chuck_norris_joke_api import ChuckNorrisJokeApi
from third_parties.jokes.models.base_joke_api import BaseJokeApi


def get_remote_joke_api() -> BaseJokeApi:
  return ChuckNorrisJokeApi()
