# app/models/reading_history_model.py
from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.dal.database import db

class ReadingHistory(db.Model):
    __tablename__ = 'reading_history'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    book_id = Column(Integer, nullable=False)
    rating = Column(Float, nullable=True)
    
    user = relationship('User', back_populates='reading_history')
