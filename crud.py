from sqlalchemy.orm import Session 
from . import models, schemas
from datetime import datetime, timezone

#---CRUD User---

#Create_User
def create_users(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name = user.name,
        email=user.email,
        password=user.password,
        create_at = datetime.now(timezone.utc)
    ) 
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user 

#Get_User
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

#Update_User
def update_user(db: Session, user_id: int, user_update: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db_user.name = user_update.name 
        db_user.email = user_update.email
        db_user.password = user_update.password
        db.commit()
        db.refresh(db_user)
    return db_user 

#Delete_User
def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    
#---CRUD List---
def create_list(db: Session, list_in: schemas.ListCreate):
    db_lists = models.List(
        title = list_in.title,
        category = list_in.category,
        description = list_in.description,
        created_at = datetime.now(timezone.utc)
    )
    db.add(db_lists)
    db.commit()
    db.refresh(db_lists)
    return db_lists

def get_list(db: Session, list_id: int):
    return db.query(models.List).filter(models.List.id == list_id).first()

def get_list(db:Session, skip: int=0, limit: int=100):
    return db.query(models.List).offset(skip).limit(limit).all()

#---CRUD Task---
def create_task(db: Session, task_in: schemas.TaskCreate):
    db_task = models.Task(
        title=task_in.title,
        description=task_in.description,
        due_date=task_in.due_date,
        priority=task_in.priority,
        status=task_in.status,
        user_id=task_in.user_id,   # foreign key
        list_id=task_in.list_id,   # foreign key
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc)
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def get_task(db: Session, skip: int=0, limit: int=100):
    return db.query(models.Task).offset(skip).limit(limit).all()
