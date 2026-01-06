from sqlmodel import Field, SQLModel, Enum, Column
from pydantic import EmailStr
import enum


class Role(enum.Enum):
    User = "user"
    Author = "author"
    Admin = "admin"


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    email: EmailStr = Field(unique=True, index=True)
    role: str = Field(Column(type_=Role, default="user"))
    # name, username email, role, etc
