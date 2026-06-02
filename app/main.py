from fastapi import FastAPI
from app.routers.todos import router as todo_router
from app.database.connection import Base, engine
from app.models import todo

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todo_router)