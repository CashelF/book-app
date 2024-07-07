# app/models/user_preferences_embedding_model.py

from app.dal.database import db

class UserPreferencesEmbedding(db.Model):
    __tablename__ = 'user_preferences_embeddings'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    embedding = db.Column(db.LargeBinary, nullable=False)  # Store embeddings as binary data
    
    user = db.relationship('User', back_populates='preferences_embedding')
