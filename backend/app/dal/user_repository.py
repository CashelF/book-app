from app.models.user_model import User, db

class UserRepository:
    def get_user_by_id(self, user_id):
        return User.query.get(user_id)

    def add_user(self, username, email, password):
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return new_user.id

    def update_user(self, user_id, username, email):
        user = User.query.get(user_id)
        if user:
            user.username = username
            user.email = email
            db.session.commit()
            return True
        return False

    def delete_user(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
    
    def get_user_by_email(self, email):
        return User.query.filter_by(email=email).first()
