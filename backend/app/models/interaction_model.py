# app/models/interaction_model.py
from app.dal.database import db
from enum import Enum
from sqlalchemy.sql import text

class InteractionType(Enum):
    LIKE = 'like'
    SAVE = 'save'
    VIEW = 'view'

class Interaction(db.Model):
    __tablename__ = 'interactions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False, index=True)
    interaction_type = db.Column(db.Enum(InteractionType), nullable=False, index=True)
    timestamp = db.Column(db.DateTime, nullable=True)
    duration = db.Column(db.Integer, nullable=True)  # Duration in seconds for 'view' interactions
    
    user = db.relationship('User', back_populates='interactions')
    book = db.relationship('Book', back_populates='interactions')
