from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.dal.database import db
from .associations.content_author_association import content_author_association

class Author(db.Model):
    __tablename__ = 'author'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    contents = relationship('Content', secondary=content_author_association, back_populates='authors')
