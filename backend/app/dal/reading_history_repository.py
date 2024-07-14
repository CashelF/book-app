from app.models.reading_history_model import ReadingHistory
from app.dal.database import db

class ReadingHistoryRepository:

    @staticmethod
    def add_reading_history(user_id, book_id):
        reading_history = ReadingHistory(user_id=user_id, book_id=book_id)
        db.session.add(reading_history)
        db.session.commit()
