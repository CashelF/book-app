import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "jungK00K!",
    database = "books_db"
)

cursor = db.cursor()
