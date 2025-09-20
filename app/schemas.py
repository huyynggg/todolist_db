from pydantic import BaseModel, EmailStr
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

# USERS
class UserBase(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserCreate(UserBase):
    # This class inherits all fields from UserBase, so the password field is redundant here.
    pass

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    # IMPORTANT: Do not include the password field in the response schema for security.
    created_at: datetime

    class Config:
        # Pydantic V2 uses 'from_attributes' instead of the deprecated 'orm_mode'.
        from_attributes = True

# LISTS
class ListBase(BaseModel):
    title: str
    category: Optional[str] = None
    description: Optional[str] = None

class ListCreate(ListBase):
    pass 

class List(ListBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# TASKS
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    priority: Optional[TaskPriority] = TaskPriority.medium
    status: Optional[TaskStatus] = TaskStatus.pending 

class TaskCreate(TaskBase):
    list_id: int
    user_id: int 

class Task(TaskCreate):
    id: int
    # The 'user_id' and 'list_id' fields are already in TaskCreate, so they're redundant here.
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True