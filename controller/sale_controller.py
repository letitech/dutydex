from tkinter import messagebox
from model.sale import Sale

class SaleController():
    def __init__(self):
        self.sale = Sale()
            
    def create(self, user, products, date):
        if user and products and date:
            for product, quantity in products.items():                
                if self.sale.create(user, product, quantity, date):
                    # messagebox.showinfo("Éxito", "Venta registrada exitosamente")
                    return True
                else:
                    # messagebox.showwarning("Error", "No se pudo guardar el registro")
                    return False
        else:
            messagebox.showerror("Compos vacíos", "Por favor, rellene todos los campos")
            
    def read(self):
        return self.sale.read()