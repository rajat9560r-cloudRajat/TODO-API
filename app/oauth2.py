import jwt
from jwt import InvalidTokenError
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from . import models
from fastapi import Depends, HTTPException, status
from .database import get_db
from fastapi.security import OAuth2PasswordBearer
lee_aao_token = OAuth2PasswordBearer(tokenUrl = '/login')

load_dotenv()


ALGORITHM = os.getenv("ALGO")
SECRET_KEY = os.getenv("SECRET_KEY")
EXPIRATION_TIME  = 30

def create_access_token(data : dict):
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(minutes = EXPIRATION_TIME)
    payload["exp"] = expire
    access_token = jwt.encode(payload, SECRET_KEY, algorithm = ALGORITHM)
    
    return access_token

def verify_access_token(token : str, credentials_exception):
    try:
        token_breakdown = jwt.decode(token, SECRET_KEY, algorithms = [ALGORITHM])
        user_id = token_breakdown.get("id")
        if not user_id:
            raise credentials_exception   
    except InvalidTokenError:
        credentials_exception  
    return user_id

def get_current_user(token : str = Depends(lee_aao_token)):
    credentials_exception = HTTPException(status.HTTP_401_UNAUTHORIZED, 
                detail = "Credentials didn't match, try again", headers = {"WWW-Authenticate":"Bearer"})
    return verify_access_token(token, credentials_exception)