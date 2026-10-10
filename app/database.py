from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine 
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('DB_URL')

engine = create_engine(url)

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind = engine)


class Base(DeclarativeBase):
    pass

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
