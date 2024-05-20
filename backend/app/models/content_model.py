from sqlalchemy import Column, Integer, String, Enum, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from app.dal.database import Base

class Content(Base):
    __tablename__ = 'content'
    
    content_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255))
    type = Column(Enum('book', 'article'))
    genre = Column(String(100))
    publication_year = Column(Integer)
    description = Column(Text)
    cover_image_url = Column(String(255))
    
    interactions = relationship("Interaction", back_populates="content")
    features = relationship("ContentFeature", back_populates="content")
