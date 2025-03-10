from tkinter import messagebox
from model.product import Product

class ProductController():
    def __init__(self):
        self.product = Product()
            
    def create(self, name, description, price, stock):
        if name and price and stock:
            if self.product.create(name, description, price, stock):
                messagebox.showinfo("Éxito", "Producto registrado exitosamente")
                return True
            else:
                messagebox.showwarning("Error", "No se pudo guardar el registro")
        else:
            messagebox.showerror("Compos vacíos", "Por favor, rellene todos los campos")
            
    def read(self):
        return self.product.read()
    
    def read_by_id(self, id):
        if id:
            product = self.product.read_by_id(id)
            if len(product) == 0:
                messagebox.showwarning("Error", "Producto no encontrado")
            else:
                return self.product.read_by_id(id)
        else:
            messagebox.showerror("Compos vacíos", "Por favor, rellene todos los campos")
            
    def add_to_cart(self, id, quantity):
        if id and quantity:
            product = self.product.read_by_id(id)
            if len(product) == 0:
                messagebox.showwarning("Error", "Producto no encontrado")
            else:
                if int(quantity) > product[0][4]:
                    messagebox.showwarning("Error", "No hay suficiente stock")
                else:
                    result = self.product.read_by_id(id)
                    details = [result[0][0], result[0][1], result[0][3], quantity, result[0][3] * int(quantity)]
                    return details
        else:
            messagebox.showerror("Compos vacíos", "Por favor, rellene todos los campos")