from sqlite3 import *

class Database:

    def __init__(self):
        self.connection = connect('./stories.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS stories(
        id INTEGER PRIMARY KEY,
        title TEXT UNIQUE,
        file TEXT UNIQUE,
        send_count INTEGER);""")
        self.connection.commit()


    def insert(self, title, file, send_count=0):
        self.cursor.execute("""
        INSERT INTO stories(title, file, send_count)
        VALUES(?, ?, ?)""", (title, file, send_count,))
        self.connection.commit()

    def find(self, title) -> tuple:
        self.cursor.execute("SELECT * FROM stories WHERE title=?", (title,))
        return self.cursor.fetchone()

    def update(self, title, field, value):
        self.cursor.execute(f"UPDATE stories SET {field}=? WHERE title=?", (value, title,))
        self.connection.commit()

    def delete(self, title):
        self.cursor.execute("DELETE FROM stories WHERE title=?", (title,))
        self.connection.commit()