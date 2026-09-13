from pydantic import BaseModel



class Validation(BaseModel):
    kaam : str
    name : str

class Response(BaseModel):
    id : int
    name : str

class Update(BaseModel):
    kaam : str | None = None
    name : str | None = None