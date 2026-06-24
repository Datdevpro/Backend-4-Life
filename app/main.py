from fastapi import FastAPI
from app.database.connection import Base, engine
#from app.models import todo
from app.models import user, conversation, message, todo
from app.routers import auth
from app.routers.conversations import router as conversation_router
from app.routers.todos import router as todo_router
from app.routers.messages import router as message_router

Base.metadata.create_all(bind=engine)

tags_metadata = [
    {"name": "Auth"},
    {"name": "Todos"},
    {"name": "Conversations"}, 
    {"name": "Messages"}


]

app = FastAPI(openapi_tags=tags_metadata)

app.include_router(auth.router)
app.include_router(todo_router)
app.include_router(conversation_router)
app.include_router(message_router)
