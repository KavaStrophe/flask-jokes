from typing import List, Optional
from third_parties.jokes.models.remote_joke import RemoteJoke
import requests


class BaseJokeApi:
  url: str
  source:str
  
  def __init__(self) -> None:
    pass
  
  def search(self, query:str, page:int, per_page:int) -> List[RemoteJoke]:
    """List jokes from remote source"""
    pass
  
  def get(self, id: str) -> Optional[RemoteJoke]:
    """Get joke from remote source"""
    pass
  
  def base_request(self, method: str, path:str, params:Optional[dict] = None ):
    url = self.url + path
    print("Requesting: [", method, "] ", url )
    response = requests.request(method, url, params=params)
    print(response.url)
    if response.status_code // 100 == 2:  # Check if status code is in the 200 family
        return response.json()
    if response.status_code == 404:
      return None
    else:
        raise Exception(f"Request failed with status code: {response.status_code}")
