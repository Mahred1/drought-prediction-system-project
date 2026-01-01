from sqlmodel import Field, SQLModel, Relationship


class Article(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)