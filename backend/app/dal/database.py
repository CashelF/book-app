import pymysql
from pymysql.cursors import DictCursor

class Database:
    def __init__(self, host='localhost', user='your_user', password='your_password', db='your_db'):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def __enter__(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, cursorclass=DictCursor)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

