from .database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, func

class Todo(Base):
    __tablename__ = "todotodo"
    id = Column(Integer, primary_key = True, nullable = False)
    todo = Column(String, unique=True,nullable=False)
    created_at = Column(TIMESTAMP, nullable = False, server_default=func.now())

class User(Base):
    __tablename__="usertodo"
    id = Column(Integer, primary_key = True, nullable = False)
    name = Column(Integer, nullable = False)
    email = Column(String,unique=True, nullable = False)
    password = Column(String, nullable = False)
    created_at = Column(TIMESTAMP, nullable = False, server_default=func.now())
