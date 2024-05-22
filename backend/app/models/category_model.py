from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.dal.database import db
from .associations.content_category_association import content_category_association

class Category(db.Model):
    __tablename__ = 'category'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    contents = relationship('Content', secondary=content_category_association, back_populates='categories')
