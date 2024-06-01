# app/models/preference_model.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.dal.database import db

class Preference(db.Model):
    __tablename__ = 'preferences'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    genre = Column(String(50), nullable=True) # TODO: replace with relationship for all of these
    author = Column(String(255), nullable=True)
    
    user = relationship('User', back_populates='preferences')
