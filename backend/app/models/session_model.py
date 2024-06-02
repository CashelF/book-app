# app/models/session_model.py
from app.dal.database import db

class Session(db.Model):
    __tablename__ = 'sessions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    time_of_day = db.Column(db.Integer, nullable=True)
    day_of_week = db.Column(db.Integer, nullable=True)
    device_type = db.Column(db.String(50), nullable=True)
    duration = db.Column(db.Float, nullable=True)
    
    user = db.relationship('User', back_populates='sessions')
