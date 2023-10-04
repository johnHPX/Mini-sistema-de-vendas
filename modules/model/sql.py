import sqlite3

class Database():
    def __init__(self) -> None:
        self.conn = sqlite3.connect('database/dat.db')

    def connect_db(self):
        return self.conn

