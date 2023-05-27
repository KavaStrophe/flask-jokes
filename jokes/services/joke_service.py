from typing import Any, Optional, List
from jokes.models.joke_model import JokeModel
from third_parties.jokes.models.base_joke_api import BaseJokeApi
from third_parties.jokes.remote_joke_api import get_remote_joke_api


class JokeService:
  remote_joke_api: BaseJokeApi
  
  def __init__(self):
    self.remote_joke_api = get_remote_joke_api()
    
  def get(self, joke_id: str) -> Optional[Any]:
    result: Optional[JokeModel] = JokeModel.query.filter_by(id = joke_id).first()
    if(result != None):
      return result
    return self.remote_joke_api.get(joke_id)
    
  def search(self, query: str, page: int, per_page:int) -> List[Any]:
    result: Optional[JokeModel] = JokeModel.query.filter(JokeModel.content.like("%{}%".format(query))).paginate(
        page=page, per_page=per_page).items
    if(result != None):
      return result
    return self.remote_joke_api.search(query=query, page=page, per_page=per_page)
    
