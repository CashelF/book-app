from dal.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.user_repo = UserRepository()

    def get_user(self, user_id):
        """
        Retrieves a user by their ID.
        """
        user = self.user_repo.get_user_by_id(user_id)
        if user:
            return user
        else:
            raise ValueError("User not found")

    def create_user(self, name, email):
        """
        Creates a new user with the given name and email.
        """
        user_id = self.user_repo.add_user(name, email)
        return self.get_user(user_id)

    def update_user(self, user_id, name, email):
        """
        Updates an existing user's name and email.
        """
        update_count = self.user_repo.update_user(user_id, name, email)
        if update_count == 0:
            raise ValueError("User update failed or user not found")
        return self.get_user(user_id)

    def delete_user(self, user_id):
        """
        Deletes a user by their ID.
        """
        delete_count = self.user_repo.delete_user(user_id)
        if delete_count == 0:
            raise ValueError("User deletion failed or user not found")
        return {"success": True, "message": "User deleted successfully"}

    def list_users(self):
        """
        Lists all users in the database.
        """
        return self.user_repo.get_all_users()
    
    def get_user_by_email(self, email):
        user = self.user_repo.get_user_by_email(email)
        if not user:
            raise ValueError("No user found with the given email")
        return user
