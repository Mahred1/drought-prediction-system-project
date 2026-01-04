from sqlmodel import Field, Column, SQLModel, Relationship, Enum as SQLEnum
from User import User
from config.database_config import create_table
from pydantic import BaseModel
from typing import Optional, List


class ArticleModel(BaseModel):
    id: Optional[int]
    title: str
    body: str
    tags: Optional[List]
    author_id: int




class Article(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field( max_length=100)
    body: str |None
    tags: List | None
    author_id: int = Field(foreign_key='User.id')
    author: User = Relationship(cascade_delete=True, back_populates="User")
    
    
    
    


if __name__ == "__main__":
    create_table()