from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class UserModel(Base):
    __tablename__ = 'users'

   # Primary key
    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True )
    
    password_hash = Column(String)

    
