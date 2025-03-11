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
    
    def read_by_username(self, username):
        if username:
            result = self.user.read_by_username(username)
            if len(result) == 0:
                messagebox.showwarning("Error", "Este usuario no existe")
            else:
                return result
        else:
            messagebox.showerror("Compos vacíos", "Por favor, rellene todos los campos")
    
    def update(self, id, name, lastname, username, password):
        if name and lastname and username and password:
            if self.user.update(id, name, lastname, username, password):
                messagebox.showinfo("Éxito", "Usuario actualizado exitosamente")
                return True
            else:
                messagebox.showwarning("Error", "No se pudo actualizar el registro")
        else:
            messagebox.showerror("Compos vacíos", "Por favor, rellene todos los campos")