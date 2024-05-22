from sqlalchemy import Column, Integer, String, Float, Enum, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.dal.database import db
from .associations.saved_books_association import saved_books

class User(db.Model):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, default=func.now())
    age = Column(Integer, nullable=True)
    gender = Column(Enum('male', 'female', 'other'), nullable=True)
    location_latitude = Column(Float, nullable=True)
    location_longitude = Column(Float, nullable=True)
    average_rating = Column(Float, nullable=True)
    number_of_books_read = Column(Integer, nullable=True)
    device_type = Column(String(50), nullable=True)
    theme = Column(String(50), nullable=True)
    font_size = Column(String(50), nullable=True)
    click_through_rate = Column(Float, nullable=True)
    engagement_rate = Column(Float, nullable=True)

    # Relationships
    reading_history = relationship('ReadingHistory', back_populates='user')
    interactions = relationship('Interaction', back_populates='user')
    preferences = relationship('Preference', back_populates='user')
    sessions = relationship('Session', back_populates='user')
    saved_books = relationship('Content', secondary=saved_books, back_populates='saved_by_users')
