from fastapi import APIRouter, Depends, HTTPException, status, Response
from .. import models, utils, schemas, oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
router = APIRouter(
    prefix = '/login',
    tags = ['authentication']
)

'''
The OAuth2PasswordRequestForm is a built-in FastAPI dependency [1] class used to automatically 
parse, validate, and secure the user credentials (username and password) sent during a login
request.Instead of creating a custom Pydantic model to handle login data'''

@router.post("", response_model = schemas.LoginResponse)
def user_login(credentials:OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email==credentials.username).first()
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail = "Idk but stmg is wrong with your credentials")
    if not utils.verify(credentials.password, user.password):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail = "Idk but stmg is wrong with your credentials")
    token = oauth2.create_access_token({"id": user.id})
    print("Name of the user accessing: ",user.name)
    return {"access_token":token, "type":"Bearer"}


           