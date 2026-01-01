from sqlmodel import create_engine
from dotenv import load_dotenv
import os
load_dotenv()



POSTGRES_URL = os.getenv('POSTGRES_URL')

engine = create_engine(POSTGRES_URL)

if(engine):
    print(engine)