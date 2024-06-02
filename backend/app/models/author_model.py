# app/models/author_model.py
from app.dal.database import db
from .associations.content_author_association import content_author_association

class Author(db.Model):
    __tablename__ = 'author'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    contents = db.relationship('Content', secondary=content_author_association, back_populates='authors')
