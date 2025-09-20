# Correct users.py code

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from app.db import (get_db) 

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/", response_model=list[schemas.User])
def read_user(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    user = crud.get_user(db=db, skip=skip, limit=limit)
    return user