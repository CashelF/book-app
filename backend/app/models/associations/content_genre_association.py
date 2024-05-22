from sqlalchemy import Table, Column, Integer, ForeignKey
from app.dal.database import db

content_genre_association = Table('content_genre_association', db.Model.metadata,
    Column('content_id', Integer, ForeignKey('content.id'), primary_key=True),
    Column('genre_id', Integer, ForeignKey('genre.id'), primary_key=True)
)
