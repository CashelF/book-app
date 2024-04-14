import mysql.connector

db = mysql.connector.connect(
    host = "127.0.0.1:3306",
    user = "root",
    password = "jungK00K!",
    database = "books_db"
)

cursor = db.cursor()
