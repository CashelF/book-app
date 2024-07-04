from app.dal.database import db

class BookParameters(db.Model):
    __tablename__ = 'book_parameters'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    parameters = db.Column(db.LargeBinary, nullable=False)
    book = db.relationship('Book', back_populates='parameters')
