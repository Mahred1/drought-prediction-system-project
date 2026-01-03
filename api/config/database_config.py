from sqlmodel import create_engine, SQLModel
from dotenv import load_dotenv
import os
load_dotenv()



POSTGRES_URL = os.getenv('POSTGRES_URL')

engine = create_engine(POSTGRES_URL, echo=True)


def create_table():
    SQLModel.metadata.create_all(engine)