# app/dal/user_repository.py
from app.models.user_model import User
from app.dal.database import SessionLocal

def add_user(user):
    session = SessionLocal()
    session.add(user)
    session.commit()
    session.close()

def get_user_by_email(email):
    session = SessionLocal()
    user = session.query(User).filter_by(email=email).first()
    session.close()
    return user

def get_user_by_id(user_id):
    session = SessionLocal()
    user = session.query(User).get(user_id)
    session.close()
    return user
