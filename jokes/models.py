from datetime import datetime
from typing import  Optional
from sqlalchemy import Column, DateTime, Integer, Text, VARCHAR
from flask_sqlalchemy.model import Model

from lib.db import db

class JokeModel(db.Model, Model):
  __tablename__ = 'jokes'
  
  id = Column[int](Integer, primary_key=True, name="joke_id")
  source  = Column[str](VARCHAR(191), name="source", default="local")
  content = Column[str](Text, name="content")
  created_at = Column[datetime](DateTime, name="created_at")
  updated_at = Column[datetime](DateTime, name="updated_at")
  deleted_at= Column[Optional[datetime]](DateTime, nullable=True, name="deleted_at")
  
  def __json__(self) -> dict:
    return {
      "id": self.id,
      "source": self.source,
      "content": self.content,
      "categories": [],
      "created_at": self.created_at.isoformat(),
      "updated_at": self.updated_at.isoformat(),
      "deleted_at": self.deleted_at.isoformat() if self.deleted_at != None else self.deleted_at
    }
