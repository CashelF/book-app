# app/models/associations/content_category_association.py
from sqlalchemy import Table, Column, Integer, ForeignKey
from app.dal.database import db

content_category_association = Table('content_category_association', db.Model.metadata,
    Column('content_id', Integer, ForeignKey('content.id'), primary_key=True),
    Column('category_id', Integer, ForeignKey('category.id'), primary_key=True)
)
