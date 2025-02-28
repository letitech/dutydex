from tkinter import Tk, Label, Entry, Button
from tkinter.ttk import Notebook, Frame, Treeview
from controller import user_controller, product_controller

class Dashboard(Tk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        self.minsize(800, 600)
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        x = str(round((screen_width - 800) / 2))
        y = str(round((screen_height - 600) / 2))
        
        self.geometry(f"800x600+{x}+{y}")
        
        self.notebook = Notebook(self)
        self.notebook.pack(fill="both", expand=True)
        
        self.user_tab() 
        self.read_users()
        
        self.product_tab()
        self.read_products()
        
    def user_tab(self):
        tab1 = Frame(self.notebook)
        self.notebook.add(tab1, text = "Usuarios")
        
        head_frame = Frame(tab1)
        head_frame.pack(fill="x", expand=True, pady=10, padx=10)
        
        self.label_creator(head_frame, "Nombre", 0, 0)
        self.name_entry = self.entry_creator(head_frame, 1, 0)
        
        self.label_creator(head_frame, "Apellidos", 0, 1)
        self.lastname_entry = self.entry_creator(head_frame, 1, 1)
        
        self.label_creator(head_frame, "Usuario", 0, 2)
        self.username_entry = self.entry_creator(head_frame, 1, 2)
        
        self.label_creator(head_frame, "Contraseña", 0, 3)
        self.password_entry = Entry(head_frame, width=35, show="*")
        self.password_entry.grid(column=1, row=3, pady=10)
        
        save_button = Button(head_frame, text="Guardar", command=self.create_user)
        save_button.grid(row=4, columnspan=2, pady=10)
        
        body_frame = Frame(tab1)
        body_frame.pack(fill="x", expand=True, padx=10)
        
        self.treeview = Treeview(body_frame, columns=("Nombre", "Apellidos", "Usuario"))
        self.treeview.pack(fill="x", expand=True)
        self.treeview.heading("#0", text="ID")
        self.treeview.heading("#1", text="Nombre")
        self.treeview.heading("#2", text="Apellidos")
        self.treeview.heading("#3", text="Usuario")

    def product_tab(self):
        tab1 = Frame(self.notebook)
        self.notebook.add(tab1, text = "Productos")
        
        head_frame = Frame(tab1)
        head_frame.pack(fill="x", expand=True, pady=10, padx=10)
        
        self.label_creator(head_frame, "Nombre", 0, 0)
        self.name_entry = self.entry_creator(head_frame, 1, 0)
        
        self.label_creator(head_frame, "Descripción", 0, 1)
        self.descripcion_entry = self.entry_creator(head_frame, 1, 1)
        
        self.label_creator(head_frame, "Precio", 0, 2)
        self.price_entry = self.entry_creator(head_frame, 1, 2)
        
        self.label_creator(head_frame, "Stock", 0, 3)
        self.stock_entry = self.entry_creator(head_frame, 1, 3)
        
        save_button = Button(head_frame, text="Guardar", command=self.create_product)
        save_button.grid(row=4, columnspan=2, pady=10)
        
        body_frame = Frame(tab1)
        body_frame.pack(fill="x", expand=True, padx=10)
        
        self.treeview = Treeview(body_frame, columns=("Nombre", "Descripción", "Precio", "Stock"))
        self.treeview.pack(fill="x", expand=True)
        self.treeview.heading("#0", text="ID")
        self.treeview.heading("#1", text="Nombre")
        self.treeview.heading("#2", text="Descripción")
        self.treeview.heading("#3", text="Precio")
        self.treeview.heading("#4", text="Stock")
    
    def label_creator(self, father, name, column, row):
        Label(father, text=name).grid(column=column, row=row, pady=10, padx=10, sticky="w")
    
    def entry_creator(self, father, column, row):
        entry = Entry(father, width=35)
        entry.grid(column=column, row=row, pady=10)
        return entry
    
    def button_creator(self, father, name, column, row):
        button = Button(father, text=name)
        button.grid(column=column, row=row, pady=10, padx=10)
        return button
    
    def create_user(self):
        controller = user_controller.UserController()
        if controller.create(self.name_entry.get(), self.descripcion_entry.get(), self.price_entry.get(), self.password_entry.get()):
            self.name_entry.delete(0, "end")
            self.descripcion_entry.delete(0, "end")
            self.price_entry.delete(0, "end")
            self.password_entry.delete(0, "end")
            self.read_users()

    def create_product(self):
        controller = product_controller.ProductController()
        if controller.create(self.name_entry.get(), self.descripcion_entry.get(), self.price_entry.get(), self.stock_entry.get()):
            self.name_entry.delete(0, "end")
            self.descripcion_entry.delete(0, "end")
            self.price_entry.delete(0, "end")
            self.stock_entry.delete(0, "end")
            self.read_products()
        
    def read_users(self):
        controller = user_controller.UserController()
        for registro in self.treeview.get_children():
            self.treeview.delete(registro)
        
        for registro in controller.read():
            self.treeview.insert("", "end", text=registro[0], values=registro[1:])
    
    def read_products(self):
        controller = product_controller.ProductController()
        for registro in self.treeview.get_children():
            self.treeview.delete(registro)
        
        for registro in controller.read():
            self.treeview.insert("", "end", text=registro[0], values=registro[1:])