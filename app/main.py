from fastapi import FastAPI
from app.routers.todos import router as todo_router
from app.database.connection import Base, engine
from app.models import todo
from app.models import user
from app.routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todo_router)
app.include_router(auth.router)