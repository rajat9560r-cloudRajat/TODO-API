from pydantic import BaseModel
from pydantic import EmailStr
from datetime import datetime

class Validation(BaseModel):
    todo : str
    

class Response(BaseModel):
    id : int
    todo : str
    created_at:datetime
    

class Update(BaseModel):
    todo : str | None = None
    

class Put(Validation):
    pass

#===============USER SCHEMA================================
class UserValidation(BaseModel):
    name : str
    email : EmailStr
    password : str

class UserResponse(BaseModel):
    id : int
    name : str
    email : EmailStr
    

class UserUpdate(BaseModel):
    name : str | None = None
    email : EmailStr| None = None
    password : str| None = None