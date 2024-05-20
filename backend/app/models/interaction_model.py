from sqlalchemy import Column, Integer, ForeignKey, Enum, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.dal.database import Base

class Interaction(Base):
    __tablename__ = 'interactions'
    
    interaction_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    content_id = Column(Integer, ForeignKey('content.content_id'))
    interaction_type = Column(Enum('view', 'like', 'save', 'purchase'))
    created_at = Column(TIMESTAMP, default=func.now())
    
    user = relationship("User", back_populates="interactions")
    content = relationship("Content", back_populates="interactions")
