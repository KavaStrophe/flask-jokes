from datetime import datetime
from typing import List, Optional
from sqlalchemy import Column, DateTime, Integer, Text, VARCHAR
from flask_sqlalchemy.model import Model

from lib import db

class JokeModel(db.Model, Model):
  __tablename__ = 'jokes'
  
  id = Column[int](Integer, primary_key=True, name="joke_id")
  external_id  = Column[str](VARCHAR(191), nullable=True)
  source  = Column[str](VARCHAR(191), default="local")
  content = Column[str](Text)
  created_at = Column[datetime](DateTime)
  updated_at = Column[datetime](DateTime)
  deleted_at= Column[Optional[datetime]](DateTime, nullable=True)
  
  def __json__(self) -> dict:
    return {
      "id": self.external_id,
      "content": self.content,
      "categories": [],
      "created_at": self.created_at,
      "updated_at": self.updated_at,
      "deleted_at": self.deleted_at
    }
