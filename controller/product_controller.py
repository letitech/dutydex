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