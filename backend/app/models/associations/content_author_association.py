from sqlalchemy import Table, Column, Integer, ForeignKey
from app.dal.database import db

content_author_association = Table('content_author_association', db.Model.metadata,
    Column('content_id', Integer, ForeignKey('content.id'), primary_key=True),
    Column('author_id', Integer, ForeignKey('author.id'), primary_key=True)
)
