from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.dal.database import db

class Interaction(db.Model):
    __tablename__ = 'interactions'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    content_id = Column(Integer, ForeignKey('content.id'), nullable=False)
    interaction_type = Column(String(50), nullable=False)  # e.g., 'like', 'save', 'view'
    reward = Column(Float, nullable=False)
    timestamp = Column(Date, nullable=True)
    
    user = relationship('User', back_populates='interactions')
    content = relationship('Content', back_populates='interactions')
