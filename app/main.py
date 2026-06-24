from fastapi import FastAPI
from app.database.connection import Base, engine
from app.models import todo
from app.models import user
from app.routers import auth
from app.routers.todos import router as todo_router

Base.metadata.create_all(bind=engine)

tags_metadata = [
    {"name": "Auth"},
    {"name": "Todos"},
]

app = FastAPI(openapi_tags=tags_metadata)

app.include_router(auth.router)
app.include_router(todo_router)
