from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from enum import Enum 

class TaskPriority(str, Enum):
    high = 'High'
    medium = 'Medium'
    low = 'Low'

class TaskStatus(str, Enum):
    pending = 'Pending'
    in_progress = 'In Progress'
    done = 'Done'

#USERS
class UserBase(BaseModel):
    name: str
    email: str
    password: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

#List
class ListsBase(BaseModel):
    title: str
    category: Optional[str]=None
    description: Optional[str]=None

class ListsCreate(ListsBase):
    pass 

class Lists(ListsBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

#Tasks
class TasksBase(BaseModel):
    title: str
    description: Optional[str]
    due_date: Optional[datetime]
    priority: Optional[TaskPriority] = TaskPriority.medium
    status: Optional[TaskStatus] = TaskStatus.pending 

class TasksCreate(TasksBase):
    list_id: int
    user_id: int 

class Tasks(TasksCreate):
    id: int
    user_id: int 
    list_id: int 
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True 
    

