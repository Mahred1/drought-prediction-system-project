from Article import Article
from sqlmodel import Session, select, col
from config.database_config import engine
from sqlalchemy import exc
from pydantic import PastDate
from typing import Optional, List


class ArticleMethods:
    """A Class for CRUD Operations in Article schema"""

    def __init__(self, engine=engine):
        self.engine = engine

    @staticmethod
    async def create_new_article(data: Article, engine=engine, *args, **kwargs):

        if not data:
            raise Exception(
                "Static Method 'create_new_article()' expects at least data argument. none provided"
            )

        try:
            with Session(engine) as session:
                session.add(data)
                await session.commit()
                await session.refresh(data)
                return data

        except Exception as e:
            print(f"Create Article Error: {e}")
            return False

    @staticmethod
    async def Delete_article_by_id(id: int):
        if not id:
            raise Exception("id is None type")
        try:
            with Session(engine) as session:
                target_article = await session.get(Article, id)
                await session.delete(target_article)
                return target_article

        except exc.NoResultFound as e:
            print("No Result Found")
            return False
        except exc.MultipleResultsFound as e:
            print("Happens to be multiple query result")
            # etc
            return False
        except Exception as e:
            print(e)
            return False

    @staticmethod
    async def get_own_articles(
        author_id: int, after_date: PastDate = None, offset: int = 0, limit: int = 10
    ):
        """
        Docstring of get_articles for Article Owners (Authors)

        :param after_date: to get the latest Article that are created after the given date.
        :type after_date: PastDate.
        :param offset: start row for pagination.
        :type offset: int.
        :param limit: quantity of rows for pagination.
        :type limit: int.
        """

        if not author_id:
            raise Exception("author id is none")

        try:

            isOwner = col(Article.author_id) == author_id
            afterDate = Article.created_at >= after_date
            statement = (isOwner and afterDate) if after_date else (isOwner)

            with Session(engine) as session:
                articles = await session.exec(
                    select(Article).where(statement).offset(offset).limit(limit)
                ).all()
                return articles
        except Exception as e:
            print(e)
            return False

    @staticmethod
    async def get_articles(
        tag=None, after_date: PastDate = None, offset: int = 0, limit: int = 10
    ):
        """
        Docstring of get_articles for normal users

        :param tag: the desired tag type. if None, queries all the types.
        :type tag: str.
        :param after_date: to get the latest Article that are created after the given date.
        :type after_date: PastDate.
        :param offset: start row for pagination.
        :type offset: int.
        :param limit: quantity of rows for pagination.
        :type limit: int.
        """
        try:
            statement = (tag in col(Article.tags)) or (
                col(Article.created_at) >= after_date
            )
            with Session(engine) as session:
                query = await session.exec(
                    select(Article).where(statement).offset(offset).limit(limit)
                ).all()
                return query

        except Exception as e:
            print(e)
            return False

    @staticmethod
    async def update_article(
        article_id: int,
        title: str = None,
        body: str = None,
        tags: Optional[List] = None,
    ):
        """
        Docstring for update_article (authors)

        :param article_id: primary key of the Article Model
        :type article_id: int
        :param title: to edit the title of the article
        :type title: str optional
        :param body: to edit the body of the article
        :type body: str optional
        :param tags: to edit the tag of the article
        :type tags: Optional[List]
        """
        if article_id == None:
            raise TypeError("Expected int. None was given!")

        changeTitle = title != None
        changeBody = body != None
        changeTags = tags != None
        try:

            with Session(engine) as session:
                article = await session.get(Article, article_id)
                if article == None:
                    raise exc.NoResultFound

                if changeTitle:
                    article.title = title
                if changeBody:
                    article.body = body
                if changeTags:
                    article.tags = tags
                await session.add(article)
                await session.commit()
                await session.refresh(article)
                return article

        except Exception as e:
            print(e)
            return False
