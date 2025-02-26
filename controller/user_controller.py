from tkinter import messagebox
from model.user import User

class UserController():
    def __init__(self):
        self.user = User()
        
    def login(self, username, password):
        if username and password:
            result = self.user.read_by_username(username)
            if len(result) == 0:
                messagebox.showwarning("Error", "Usuario o contraseña incorrectos")
            else:
                if password != result[0][4]:
                    messagebox.showwarning("Error", "Usuario o contraseña incorrectos")
                else:
                    return True
        else:
            messagebox.showerror("Compos vacíos", "Por favor, rellene todos los campos")
            
    def create(self, name, lastname, username, password):
        if name and lastname and username and password:
            if self.user.create(name, lastname, username, password):
                messagebox.showinfo("Éxito", "Usuario registrado exitosamente")
                return True
            else:
                messagebox.showwarning("Error", "No se pudo guardar el registro")
        else:
            messagebox.showerror("Compos vacíos", "Por favor, rellene todos los campos")
            
    def read(self):
        return self.user.read()