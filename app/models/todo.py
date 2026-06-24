from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database.connection import Base


class TodoModel(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(Boolean, default=False)
    description = Column(String, default="", nullable=True)
    
     # user_id dùng để biết todo này thuộc về user nào
    # ForeignKey("users.id") nghĩa là user_id tham chiếu đến cột id trong bảng users
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)