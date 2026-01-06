from sqlmodel import Field, Column, SQLModel, Relationship, Enum as SQLEnum
from User import User
from config.database_config import create_table
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ArticleModel(BaseModel):
    id: Optional[int]
    title: str
    body: str
    tags: Optional[List]
    author_id: int
    author: Optional[User]
    created_at: Optional[str]


class Article(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(max_length=100)
    body: str | None
    tags: List | None
    author_id: int = Field(foreign_key="User.id")
    author: User = Relationship(cascade_delete=True, back_populates="User")
    created_at: str = Field(default=datetime.now())

    def __str__(self):
        return dict(
            {
                "id": self.id,
                "title": self.title,
                "body": self.body,
                "tags": self.tags,
                "author_id": self.author_id,
                "author": self.author,
                "created_at": self.created_at,
            }
        )


if __name__ == "__main__":
    create_table()
