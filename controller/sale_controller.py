from tkinter import messagebox
from model import sale, product

class SaleController():
    def __init__(self):
        self.sale = sale.Sale()
        self.product = product.Product()
            
    def create(self, user, products, date):
        if user and products and date:
            for key, value in products.items():
                if self.sale.create(user, key, int(value[3]), date):
                    product = self.product.read_by_id(key)
                    stock = product[0][4] - int(value[3])
                    self.product.update_stock(key, stock)
        else:
            messagebox.showerror("Compos vacíos", "Por favor, rellene todos los campos")
            
    def read(self):
        return self.sale.read()
    
    def read_by_id(self, id):
        return self.sale.read_by_id(id)