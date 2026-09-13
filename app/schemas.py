from pydantic import BaseModel



class Validation(BaseModel):
    kaam : str
    name : str

class Response(BaseModel):
    id : int
    name : str