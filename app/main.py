from fastapi import FastAPI, Depends, HTTPException, Response, status
from .database import get_db, engine
from sqlalchemy.orm import Session
from . import models, schemas
from typing import List

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def first():
    return {"message":"hello world"}

@app.get("/todos", response_model=List[schemas.Response])
def get_all(db : Session = Depends(get_db)):
    tasks = db.query(models.Todo).all()
    if not tasks:
        return []
    return tasks

@app.get("/todos/{id}", response_model=schemas.Response)
def get_by_id(id:int, db : Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id==id).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail = "todo with this id not found")
    return todo


@app.post("/todos", status_code = status.HTTP_201_CREATED,response_model=schemas.Response)
def create_todo(data : schemas.Validation, db : Session = Depends(get_db)):
    todo = models.Todo(**data.model_dump())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


@app.delete("/todos/{id}")
def delete_todo(id : int, db : Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id==id).first()
    if not todo:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="nahi h be")
    db.delete(todo)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.patch("/todos/{id}", response_model=schemas.Response)
def update_todo(id : int,data : schemas.Update ,db : Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id==id).first()
    if not todo:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="nahi h be")
    new_data = data.model_dump(exclude_unset=True)
    for key, value in new_data.items():
        setattr(todo, key, value )
    db.commit()
    db.refresh(todo)
    return todo


@app.put("/todos/{id}", response_model=schemas.Put)
def update_todo(id : int,data : schemas.Update ,db : Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id==id).first()
    if not todo:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="nahi h be")
    new_data = data.model_dump()
    for key, value in new_data.items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo