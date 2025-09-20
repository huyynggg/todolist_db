from fastapi import FastAPI
from app.db import engine, Base
from app.routers import users, lists, tasks

# Create all tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}

# Include the routers for each resource
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(lists.router, prefix="/lists", tags=["lists"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])