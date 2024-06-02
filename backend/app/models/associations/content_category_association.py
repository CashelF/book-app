# app/models/associations/content_category_association.py
from app.dal.database import db

content_category_association = db.Table('content_category_association',
    db.Column('content_id', db.Integer, db.ForeignKey('content.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)
