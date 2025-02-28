from sqlite3 import connect

class DataBase():
    def __init__(self):
        self.connection = connect("db.db")
        self.create_tables()
        self.default_user()
    
    def set_connection(self):
        cursor = self.connection.cursor()
        return self.connection, cursor
    
    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                lastname TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )""")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL,
                stock INTEGER NOT NULL
            )""")
        self.connection.commit()
        
    def default_user(self):
        cursor = self.connection.cursor()
        existing_user = cursor.execute("""SELECT username FROM users WHERE username = 'dexter'""")
        
        if len(existing_user.fetchall()) == 0:  
            cursor.execute("""
                INSERT INTO users (name, lastname, username, password) 
                VALUES (?, ?, ?, ?) """, ("Daniel", "Sopale", "dexter", "dexter"))
            self.connection.commit()