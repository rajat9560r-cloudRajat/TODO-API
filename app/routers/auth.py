from fastapi import APIRouter, Depends, HTTPException, status, Response
from .. import models, utils, schemas, oauth2
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    tags = ['authentication']
)


@router.post("/login", response_model = schemas.LoginResponse)
def user_login(credentials:schemas.UserCredential, db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email==credentials.email).first()
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail = "Idk but stmg is wrong with your credentials")
    if not utils.verify(credentials.password, user.password):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail = "Idk but stmg is wrong with your credentials")
    token = oauth2.create_access_token({"id": user.id})
    print("Name of the user accessing: ",user.name)
    return {"access_token":token, "type":"Bearer"}


           