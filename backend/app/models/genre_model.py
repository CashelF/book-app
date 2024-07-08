# app/models/genre_model.py
from app.dal.database import db
from .associations.book_genre_association import book_genre_association

class Genre(db.Model):
    __tablename__ = 'genre'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    books = db.relationship('Book', secondary=book_genre_association, back_populates='genres')
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
