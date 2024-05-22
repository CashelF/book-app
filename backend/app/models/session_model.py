from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.dal.database import db

class Session(db.Model):
    __tablename__ = 'sessions'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    time_of_day = Column(Integer, nullable=True)
    day_of_week = Column(Integer, nullable=True)
    device_type = Column(String(50), nullable=True)
    duration = Column(Float, nullable=True)
    
    user = relationship('User', back_populates='sessions')
