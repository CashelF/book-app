import bcrypt

def hash_password(password):
    """Hash a password for storing."""
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password.decode('utf-8')

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user."""
    stored_password_bytes = stored_password.encode('utf-8')
    provided_password_bytes = provided_password.encode('utf-8')
    return bcrypt.checkpw(provided_password_bytes, stored_password_bytes)