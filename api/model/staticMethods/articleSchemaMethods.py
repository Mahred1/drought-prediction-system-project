from Article import ArticleSchema, ArticleModel
from sqlmodel import Session, select
from config.database_config import engine


class Article:
    """A Class for CRUD Operations in Article schema"""
    
    def __init__(self, engine=engine):
        self.engine = engine
    
    @staticmethod
    async def create_new_article(data: ArticleModel, engine=engine, *args, **kwargs):
        
        if not data:
            raise Exception("Static Method 'create_new_article()' expects at least data argument. none provided")
        
        try:
            with Session(engine) as session:
                session.add(data)
                await session.commit()
                await session.refresh(data)
            
            return data
        except Exception as e:
            print(f"Create Article Error: {e}")
            return None
    
    
    @staticmethod
    async def Delete_article_by_id(id: int):
        if not id:
            raise Exception("id is None type")
        try:
            with Session(engine) as session:
                target_article = await session.get_one(Article, {"id": id})
                await session.delete(target_article)
                return target_article
        except Exception as e:
            print(e)
            return None
        
        
    @staticmethod
    async def get_articles(author_id: int):
        if not author_id:
            raise Exception("author id is none")
        
        try:
            with Session(engine) as session:
                articles = await session.exec(select(Article).where(Article.author_id == author_id)).all()
                return articles
        except Exception as e:
            print(e)
            return False

