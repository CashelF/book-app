# app/models/author_model.py
from app.dal.database import db
from .associations.book_author_association import book_author_association

class Author(db.Model):
    __tablename__ = 'author'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    books = db.relationship('Book', secondary=book_author_association, back_populates='authors')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
