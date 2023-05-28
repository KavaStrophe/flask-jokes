from typing import  Optional
from datetime import datetime

from third_parties.jokes.models.remote_joke import RemoteJoke
from third_parties.jokes.models.base_joke_api import BaseJokeApi

  
class ChuckNorrisJokeApi(BaseJokeApi):
  def __init__(self) -> None:
    self.url = "https://api.chucknorris.io"
    self.source = "chuck_norris_api"
    
  def get(self, id: str) -> Optional[RemoteJoke]:
      joke: Optional[dict] = self.base_request("get", "/jokes/" + id)
      if (joke == None):
        return joke
      return self.map_chuck_joke_response(joke)
    
  def search(self, query: str) -> Optional[RemoteJoke]:
      jokes: Optional[dict] = self.base_request("get", "/jokes/search", {"query": query})
      if (jokes == None):
        return []
      
      return [self.map_chuck_joke_response(joke) for joke in jokes["result"]]
      
      
  def map_chuck_joke_response(self, chuck_joke:dict) -> RemoteJoke:
    return RemoteJoke(
      id = chuck_joke['id'],
      source=self.source,
      content = chuck_joke['value'],
      categories=chuck_joke['categories'],
      created_at= datetime.fromisoformat(chuck_joke['created_at']),
      updated_at= datetime.fromisoformat(chuck_joke['updated_at']),
      deleted_at=None
    )
