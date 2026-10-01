from fastapi import FastAPI, Depends, HTTPException, Response, status, APIRouter
from .database import get_db, engine
from sqlalchemy.orm import Session
from . import models, schemas, utils
from typing import List
from sqlalchemy.exc import IntegrityError

from .routers import todos, users

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(todos.router)
app.include_router(users.router)
