from sqlalchemy import Column, Integer, String, Enum, Text, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.dal.database import db

# Association tables for many-to-many relationships
content_author_association = Table('content_author_association', db.Model.metadata,
    Column('content_id', Integer, ForeignKey('content.content_id')),
    Column('author_id', Integer, ForeignKey('author.author_id'))
)

content_genre_association = Table('content_genre_association', db.Model.metadata,
    Column('content_id', Integer, ForeignKey('content.content_id')),
    Column('genre_id', Integer, ForeignKey('genre.genre_id'))
)

content_category_association = Table('content_category_association', db.Model.metadata,
    Column('content_id', Integer, ForeignKey('content.content_id')),
    Column('category_id', Integer, ForeignKey('category.category_id'))
)

class Content(db.Model):
    __tablename__ = 'content'
    
    content_id = Column(Integer, primary_key=True, autoincrement=True)
    ISBN = Column(String(13))
    title = Column(String(255), nullable=False)
    type = Column(Enum('book', 'article'))
    publication_year = Column(Integer)
    description = Column(Text)
    page_length = Column(Integer)
    cover_image_url = Column(String(255))

    authors = relationship('Author', secondary=content_author_association, back_populates='contents')
    genres = relationship('Genre', secondary=content_genre_association, back_populates='contents')
    categories = relationship('Category', secondary=content_category_association, back_populates='contents')
    interactions = relationship("Interaction", back_populates="content")