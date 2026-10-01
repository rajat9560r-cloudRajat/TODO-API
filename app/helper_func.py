from fastapi import  Depends, HTTPException, Response, status
from . import models
from sqlalchemy.orm import Session
from .database import get_db


'''helper function for USERS'''
def user_info_or_error(id:int, db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with this id not found")
    return user


'''helper function for TODOS'''
def todo_info_or_error(id:int, db:Session=Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id==id).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo with this id not found")
    return todo
