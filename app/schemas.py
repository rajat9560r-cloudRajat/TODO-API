from pydantic import BaseModel
from pydantic import EmailStr
class Validation(BaseModel):
    todo : str
    name : str

class Response(BaseModel):
    id : int
    name : str

class Update(BaseModel):
    todo : str | None = None
    name : str | None = None

class Put(Validation):
    pass

#===============================================
class UserValidation(BaseModel):
    name : str
    email : EmailStr
    password : str


class UserResponse(BaseModel):
    id : int
    email : EmailStr


class UserUpdate(BaseModel):
    name : str | None = None
    email : EmailStr| None = None
    password : str| None = None