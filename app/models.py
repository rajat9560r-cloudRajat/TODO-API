from .database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, func

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key = True, nullable = False)
    kaam = Column(String, nullable=False)
    name = Column(String, nullable = False, server_default = 'anonmous')
    created_at = Column(TIMESTAMP, nullable = False, server_default=func.now())

