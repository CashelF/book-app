from sqlalchemy.orm import sessionmaker
from models.user_model import User, engine

Session = sessionmaker(bind=engine)

class UserRepository:
    def __init__(self):
        self.session = Session()

    def get_user_by_id(self, user_id):
        return self.session.query(User).filter_by(id=user_id).first()

    def add_user(self, name, email):
        new_user = User(name=name, email=email)
        self.session.add(new_user)
        self.session.commit()
        return new_user.id

    def update_user(self, user_id, name, email):
        user = self.session.query(User).filter_by(id=user_id).first()
        if user:
            user.name = name
            user.email = email
            self.session.commit()
            return True
        return False

    def delete_user(self, user_id):
        user = self.session.query(User).filter_by(id=user_id).first()
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False
