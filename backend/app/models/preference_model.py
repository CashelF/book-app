# app/models/preference_model.py
from app.dal.database import db

class Preference(db.Model):
    __tablename__ = 'preferences'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    genre = db.Column(db.String(50), nullable=True)  # TODO: replace with relationship for all of these
    author = db.Column(db.String(255), nullable=True)
    
    user = db.relationship('User', back_populates='preferences')
