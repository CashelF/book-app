from app.dal.database import db
from app.models.user_model import User
from app.models.book_model import Book
from app.models.book_parameters_model import BookParameters

def get_user_context(user_id):
    user = User.query.get(user_id)
    return {
        'id': user.id,
        'name': user.name,
        'preferences': user.preferences
    }

def get_all_parameters():
    books = Book.query.all()
    return [{'id': book.id, 'title': book.title, 'parameters': book.parameters} for book in books]

def update_book_parameters(book_id, parameters):
    book_parameters = BookParameters.query.filter_by(book_id=book_id).first()
    book_parameters.parameters = parameters
    db.session.commit()
