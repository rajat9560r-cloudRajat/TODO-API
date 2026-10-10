from .database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__="usertodo"
    id = Column(Integer, primary_key = True, nullable = False)
    name = Column(String, nullable = False)
    email = Column(String,unique=True, nullable = False)
    password = Column(String, nullable = False)
    created_at = Column(TIMESTAMP, nullable = False, server_default=func.now())
    
class Todo(Base):
    __tablename__ = "todotodo"
    id = Column(Integer, primary_key = True, nullable = False)
    todo = Column(String, unique=True,nullable=False)
    created_at = Column(TIMESTAMP, nullable = False, server_default=func.now())
    owner_id = Column(Integer, ForeignKey('usertodo.id', ondelete='CASCADE'), nullable = False)
    owner = relationship('User')
    #here we kind of add user metadada with his/her todo


