
from sqlalchemy.orm import Session
from app import models

def get_user(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()