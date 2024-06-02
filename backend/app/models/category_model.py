# app/models/category_model.py
from app.dal.database import db
from .associations.content_category_association import content_category_association

class Category(db.Model):
    __tablename__ = 'category'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    contents = db.relationship('Content', secondary=content_category_association, back_populates='categories')
