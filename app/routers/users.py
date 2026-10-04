#libraries
from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List
from .. import models, schemas, utils
from ..database import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from ..helper_func import user_info_or_error

#router
router = APIRouter(
    prefix = '/users',
    tags = ['users']
)

#get_all
@router.get("", response_model=List[schemas.UserResponse])
def get_all(db:Session = Depends(get_db)):
    users = db.query(models.User).all()
    if not users:
        return []
    return users

#get_by_id
@router.get("/{id}", response_model=schemas.UserResponse)
def get_by_id(id:int, db:Session=Depends(get_db)):
    return user_info_or_error(id, db)

#create_new
@router.post("",status_code=status.HTTP_201_CREATED ,response_model=schemas.UserResponse)
def create_user(data:schemas.UserValidation, db:Session=Depends(get_db)):
    try:
        hashed_password = utils.hash(data.password)
        data.password = hashed_password
        user = models.User(**data.model_dump())
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="EMAIL ALREADY EXISTS!!")

#delete_by_id
@router.delete("/{id}")
def delete_user(id:int, db:Session=Depends(get_db)):
    user =  user_info_or_error(id, db)
    db.delete(user)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#update_by_id
@router.patch("/{id}", response_model=schemas.UserResponse)
def update_user(id:int,data:schemas.UserUpdate , db:Session = Depends(get_db)):
    user = user_info_or_error(id, db)
    new_data = data.model_dump(exclude_unset=True)
    #password updating
    new_hash = utils.hash(new_data["password"])
    new_data["password"] = new_hash

    for key, val in new_data.items():
        setattr(user, key, val)
    db.commit()
    db.refresh(user)
    return user
