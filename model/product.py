from config.config import DataBase

class Product():
    def __init__(self):
        self.database = DataBase()
        
    def create(self, name, description, price, stock):
        try:
            connection, cursor = self.database.set_connection()
            cursor.execute("""
                INSERT INTO products (name, description, price, stock) 
                VALUES (?, ?, ?, ?) """, (name, description, price, stock))
            connection.commit()
            return True
        except Exception as error:
            print("Error:", error)
    
    def read(self):
        try:
            connection, cursor = self.database.set_connection()
            products = cursor.execute("SELECT * FROM products")
            return products.fetchall()
        except Exception as error:
            print("Error:", error)
            
    def read_by_id(self, id):
        try:
            connection, cursor = self.database.set_connection()
            product = cursor.execute("SELECT * FROM products WHERE id = ?", (id,))
            return product.fetchall()
        except Exception as error:
            print("Error:", error)
    
    def update_stock(self, id, stock):
        try:
            connection, cursor = self.database.set_connection()
            cursor.execute("UPDATE products SET stock = ? WHERE id = ?", (stock, id))
            connection.commit()
            return True
        except Exception as error:
            print("Error:", error)