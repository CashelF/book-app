from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.dal.database import db

class Genre(db.Model):
    __tablename__ = 'genre'
    
    genre_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    contents = relationship('Content', secondary='content_genre_association', back_populates='genres')
