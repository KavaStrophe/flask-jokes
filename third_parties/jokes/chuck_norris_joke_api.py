from typing import List, Optional
from datetime import datetime

from third_parties.jokes.models.remote_joke import RemoteJoke
from third_parties.jokes.models.base_joke_api import BaseJokeApi


class ChuckNorrisJoke: 
  categories: List[str]
  created_at: str
  icon_url: str
  id: str
  updated_at: str
  url:str
  value:str
  
  
class ChuckNorrisJokeApi(BaseJokeApi):
  def __init__(self) -> None:
    self.url = "https://api.chucknorris.io"
    self.source = "chuck_norris_api"
    
  def get(self, id: str) -> Optional[RemoteJoke]:
      joke: Optional[dict] = self.base_request("get", "/jokes/" + id)
      if (joke == None):
        return joke
      print(joke)
      return self.map_chuck_joke_response(joke)
    
  def search(self, query: str, per_page:int, page:int) -> Optional[RemoteJoke]:
      jokes: Optional[dict] = self.base_request("get", "/jokes/search", {"query": query})
      if (jokes == None):
        return []
      
      # Simulate pagination as this particular API use any
      start_idx = (page - 1) * per_page
      end_idx = start_idx + per_page
      
      return [self.map_chuck_joke_response(joke) for joke in jokes["result"][start_idx:end_idx]]
      
      
  def map_chuck_joke_response(self, chuck_joke:dict) -> RemoteJoke:
    return RemoteJoke(
      id = chuck_joke['id'],
      source=self.source,
      content = chuck_joke['value'],
      categories=chuck_joke['categories'],
      url = chuck_joke['url'],
      created_at= datetime.fromisoformat(chuck_joke['created_at']),
      updated_at= datetime.fromisoformat(chuck_joke['updated_at']),
      deleted_at=None
    )
