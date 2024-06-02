# app/models/associations/content_author_association.py
from app.dal.database import db

content_author_association = db.Table('content_author_association',
    db.Column('content_id', db.Integer, db.ForeignKey('content.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
)
