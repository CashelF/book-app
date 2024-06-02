# app/models/interaction_model.py
from app.dal.database import db

class Interaction(db.Model):
    __tablename__ = 'interactions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content_id = db.Column(db.Integer, db.ForeignKey('content.id'), nullable=False)
    interaction_type = db.Column(db.Enum('like', 'save', 'view'), nullable=False)  # e.g., 'like', 'save', 'view'
    reward = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.Date, nullable=True)
    
    user = db.relationship('User', back_populates='interactions')
    content = db.relationship('Content', back_populates='interactions')
    