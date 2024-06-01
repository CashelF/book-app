# app/models/content_model.py
from sqlalchemy import Column, Integer, String, Enum, Text, Table, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from app.dal.database import db
from .associations.content_author_association import content_author_association
from .associations.content_genre_association import content_genre_association
from .associations.content_category_association import content_category_association
from .associations.saved_books_association import saved_books

class Content(db.Model):
    __tablename__ = 'content'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    ISBN = Column(String(13))
    title = Column(String(255), nullable=False)
    type = Column(Enum('book', 'article'))
    publication_year = Column(Integer)
    description = Column(Text)
    page_length = Column(Integer)
    cover_image_url = Column(String(255))
    embedding = Column(LargeBinary, nullable=True)

    authors = relationship('Author', secondary=content_author_association, back_populates='contents')
    genres = relationship('Genre', secondary=content_genre_association, back_populates='contents')
    categories = relationship('Category', secondary=content_category_association, back_populates='contents')
    interactions = relationship("Interaction", back_populates="content")
    saved_by_users = relationship('User', secondary=saved_books, back_populates='saved_books')