from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.dal.database import Base

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, default=func.now())
    
    interactions = relationship("Interaction", back_populates="user")
    preferences = relationship("UserPreference", back_populates="user")
