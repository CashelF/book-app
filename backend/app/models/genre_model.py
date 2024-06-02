# app/models/genre_model.py
from app.dal.database import db
from .associations.content_genre_association import content_genre_association

class Genre(db.Model):
    __tablename__ = 'genre'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    contents = db.relationship('Content', secondary=content_genre_association, back_populates='genres')
