from config.config import DataBase

class User():
    def __init__(self):
        self.database = DataBase()
        
    def create(self, name, lastname, username, password):
        try:
            connection, cursor = self.database.set_connection()
            cursor.execute("""
                INSERT INTO users (name, lastname, username, password) 
                VALUES (?, ?, ?, ?) """, (name, lastname, username, password))
            connection.commit()
            return True
        except Exception as error:
            print("Error:", error)
    
    def read(self):
        try:
            connection, cursor = self.database.set_connection()
            users = cursor.execute("SELECT * FROM users")
            return users.fetchall()
        except Exception as error:
            print("Error:", error)
            
    def read_by_id(self, id):
        try:
            connection, cursor = self.database.set_connection()
            user = cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
            return user.fetchall()
        except Exception as error:
            print("Error:", error)
            
    def read_by_username(self, username):
        try:
            connection, cursor = self.database.set_connection()
            user = cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            return user.fetchall()
        except Exception as error:
            print("Error:", error)
            
    def update(self, id, name, lastname, username, password):
        try:
            connection, cursor = self.database.set_connection()
            cursor.execute("UPDATE users SET name = ?, lastname = ?, username = ?, password = ? WHERE id = ?", 
                           (name, lastname, username, password, id))
            connection.commit()
            return True
        except Exception as error:
            print("Error:", error)