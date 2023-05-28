from datetime import datetime
from typing import Any, Optional, List
from uuid import uuid4
from jokes.models import JokeModel
from lib.db import db
from third_parties.jokes.models.base_joke_api import BaseJokeApi
from third_parties.jokes.remote_joke_api import get_remote_joke_api


class JokeService:
  remote_joke_api: BaseJokeApi
  
  def __init__(self):
    self.remote_joke_api = get_remote_joke_api()
    
  def get(self, id: str) -> Optional[JokeModel]:
    result: Optional[JokeModel] = JokeModel.query.filter_by(id = id).first()
    if result != None:
      print(result)
      if result.deleted_at != None:
        return None
      return result
    return self.remote_joke_api.get(id)
    
  def search(self, query: str) -> List[Any]:
    saved_jokes: List[JokeModel] = JokeModel.query.filter(JokeModel.content.like("%{}%".format(query))).all()
    ids = set(joke.id for joke in saved_jokes)
    remote_joke = self.remote_joke_api.search(query=query)
    
    # Adds the jokes not saved locally 
    for joke in remote_joke:
      if joke.id not in ids:
        saved_jokes.append(joke)
        
    # Filters deleted jokes
    return [joke for joke in saved_jokes if joke.deleted_at is None]
  
  def update(self, id:str, content:Optional[str] ) -> Optional[JokeModel]:
    existing_joke = self.get(id)
    if existing_joke == None:
      return None 
    
    if existing_joke.source != 'local':
      return self.create(content=content if content != None else existing_joke.content, id=existing_joke.id)
    
    existing_joke.content = content if content != None else existing_joke.content
    existing_joke.updated_at = datetime.now()
    db.session.commit()
    db.session.refresh(existing_joke)
    
    return existing_joke
  
  def create(self, content:str, id:Optional[str] = None, deleted_at:Optional[datetime] = None) -> JokeModel:
    joke = JokeModel()
    joke.id = id if id != None else uuid4()
    joke.source = "local"
    joke.content = content
    joke.created_at = datetime.now()
    joke.updated_at = datetime.now()
    joke.deleted_at = deleted_at
    
    db.session.add(joke)
    db.session.commit()
    db.session.refresh(joke)
    
    print(joke.id)
    
    return self.get(joke.id)
      
  def delete(self, id: str) -> bool:
    existing_joke = self.get(id)
    if existing_joke == None:
      return False 
    
    # Create locally the joke to be able to exclude it
    if existing_joke.source != 'local':
      self.create(content=existing_joke.content, id=existing_joke.id, deleted_at=datetime.now())
      return True
    
    existing_joke.updated_at = datetime.now()
    existing_joke.deleted_at = datetime.now()
    db.session.commit()
    
    return True
