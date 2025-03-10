from config.config import DataBase

class Sale():
    def __init__(self):
        self.database = DataBase()
        
    def create(self, user, product, quantity, date):
        try:
            connection, cursor = self.database.set_connection()
            cursor.execute("""
                INSERT INTO sales (user, product, quantity, date) 
                VALUES (?, ?, ?, ?) """, (user, product, quantity, date))
            connection.commit()
            return True
        except Exception as error:
            print("Error:", error)
    
    def read(self):
        try:
            connection, cursor = self.database.set_connection()
            sales = cursor.execute("SELECT sales.id, users.username, products.name, sales.quantity, sales.date FROM sales, users, products WHERE sales.user = users.id AND sales.product = products.id")
            return sales.fetchall()
        except Exception as error:
            print("Error:", error)
            
    def read_by_id(self, id):
        try:
            connection, cursor = self.database.set_connection()
            sale = cursor.execute("SELECT * FROM sales WHERE id = ?", (id,))
            return sale.fetchall()
        except Exception as error:
            print("Error:", error)