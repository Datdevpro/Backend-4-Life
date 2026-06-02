from sqlalchemy import Column, Integer, String, Boolean
from app.database.connection import Base


class TodoModel(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(Boolean, default=False)
    description = Column(String, default="", nullable=True)