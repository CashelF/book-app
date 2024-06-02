# app/dal/user_repository.py
from app.models.user_model import User
from app.dal.database import db

def add_user(user):
    db.session.add(user)
    db.session.commit()

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def get_user_by_id(user_id):
    return User.query.get(user_id)