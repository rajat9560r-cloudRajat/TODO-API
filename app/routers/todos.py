from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List
from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..helper_func import todo_info_or_error
from sqlalchemy.exc import IntegrityError
from . import auth
router = APIRouter(
    prefix = '/todos',
    tags = ['tasks']
)


@router.get("", response_model=List[schemas.Response])
def get_all(db : Session = Depends(get_db)):
    tasks = db.query(models.Todo).all()
    if not tasks:
        return []
    return tasks

@router.get("/{id}", response_model=schemas.Response)
def get_by_id(id:int, db : Session = Depends(get_db)):
    return todo_info_or_error(id, db)


@router.post("", status_code = status.HTTP_201_CREATED,response_model=schemas.Response)
def create_todo(data : schemas.Validation, db : Session = Depends(get_db)):
    try:
        todo = models.Todo(**data.model_dump())
        db.add(todo)
        db.commit()
        db.refresh(todo)
        return todo
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="TODO ALREADY EXISTS!!")
        

@router.delete("/{id}")
def delete_todo(id : int, db : Session = Depends(get_db)):
    todo = todo_info_or_error(id, db)
    db.delete(todo)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{id}", response_model=schemas.Response)
def update_todo(id : int,data : schemas.Update ,db : Session = Depends(get_db)):
    todo = todo_info_or_error(id, db)
    new_data = data.model_dump(exclude_unset=True)
    for key, value in new_data.items():
        setattr(todo, key, value )
    db.commit()
    db.refresh(todo)
    return todo


@router.put("/{id}", response_model=schemas.Put)
def update_todo(id : int,data : schemas.Update ,db : Session = Depends(get_db)):
    todo = todo_info_or_error(id, db)
    new_data = data.model_dump()
    for key, value in new_data.items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo