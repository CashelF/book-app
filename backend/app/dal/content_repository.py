# app/dal/content_repository.py
from app.models.content_model import Content
from app.dal.database import SessionLocal

def add_content(content):
    session = SessionLocal()
    session.add(content)
    session.commit()
    session.close()

def get_all_contents():
    session = SessionLocal()
    contents = session.query(Content).all()
    session.close()
    return contents

def get_content_by_id(content_id):
    session = SessionLocal()
    content = session.query(Content).get(content_id)
    session.close()
    return content

def update_content(content):
    session = SessionLocal()
    session.commit()
    session.close()

def delete_content(content):
    session = SessionLocal()
    session.delete(content)
    session.commit()
    session.close()
