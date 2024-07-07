# app/models/category_model.py
from app.dal.database import db
from .associations.book_category_association import book_category_association

class Category(db.Model):
    __tablename__ = 'category'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    books = db.relationship('Book', secondary=book_category_association, back_populates='categories')
