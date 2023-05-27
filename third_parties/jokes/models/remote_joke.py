from datetime import datetime
from typing import List, Optional


class RemoteJoke:
  id: str
  content:str
  url: str
  categories: List[str]
  created_at: datetime
  updated_at: datetime
  deleted_at: Optional[datetime]
  
  def __init__(self, id:str, content:str, url:str, categories: List[str], created_at:datetime, updated_at:datetime, deleted_at: Optional[datetime]):
    self.id = id
    self.content = content
    self.url = url
    self.categories = categories
    self.created_at = created_at
    self.updated_at = updated_at
    self.deleted_at = deleted_at
    
  def __json__(self):
    return {
      "id": self.id,
      "content": self.content,
      "url": self.url,
      "categories": self.categories,
      "created_at": self.created_at.isoformat(),
      "updated_at": self.updated_at.isoformat(),
      "deleted_at": self.deleted_at.isoformat() if self.deleted_at != None else None
    }
