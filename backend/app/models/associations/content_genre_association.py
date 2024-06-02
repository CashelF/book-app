# app/models/associations/content_genre_association.py
from app.dal.database import db

content_genre_association = db.Table('content_genre_association',
    db.Column('content_id', db.Integer, db.ForeignKey('content.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'), primary_key=True)
)
