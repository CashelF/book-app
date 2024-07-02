# app/models/user_model.py

from app.dal.database import db
from sqlalchemy.sql import func
from .associations.saved_books_association import saved_books

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=func.now())
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.Enum('male', 'female', 'other'), nullable=True)
    location_latitude = db.Column(db.Float, nullable=True)
    location_longitude = db.Column(db.Float, nullable=True)
    average_rating = db.Column(db.Float, nullable=True)
    number_of_books_read = db.Column(db.Integer, nullable=True)
    theme = db.Column(db.Enum('light', 'dark'), nullable=True)
    font_size = db.Column(db.Integer, nullable=True)
    click_through_rate = db.Column(db.Float, nullable=True)
    engagement_rate = db.Column(db.Float, nullable=True)

    # Relationships
    reading_history = db.relationship('ReadingHistory', back_populates='user')
    interactions = db.relationship('Interaction', back_populates='user')
    preferences = db.relationship('Preference', back_populates='user')
    sessions = db.relationship('Session', back_populates='user')
    saved_books = db.relationship('Book', secondary=saved_books, back_populates='saved_by_users')
    preferences_embedding = db.relationship('UserPreferencesEmbedding', back_populates='user', uselist=False)
