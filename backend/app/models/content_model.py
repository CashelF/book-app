# app/models/content_model.py
from app.dal.database import db
from .associations.content_author_association import content_author_association
from .associations.content_genre_association import content_genre_association
from .associations.content_category_association import content_category_association
from .associations.saved_books_association import saved_books

class Content(db.Model):
    __tablename__ = 'content'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ISBN = db.Column(db.String(13))
    title = db.Column(db.String(255), nullable=False)
    type = db.Column(db.Enum('book', 'article'))
    publication_year = db.Column(db.Integer)
    description = db.Column(db.Text)
    page_length = db.Column(db.Integer)
    cover_image_url = db.Column(db.String(255))
    embedding = db.Column(db.LargeBinary, nullable=True)

    authors = db.relationship('Author', secondary=content_author_association, back_populates='contents')
    genres = db.relationship('Genre', secondary=content_genre_association, back_populates='contents')
    categories = db.relationship('Category', secondary=content_category_association, back_populates='contents')
    interactions = db.relationship("Interaction", back_populates="content")
    saved_by_users = db.relationship('User', secondary=saved_books, back_populates='saved_books')
