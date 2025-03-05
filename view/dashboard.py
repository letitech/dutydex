from tkinter import Tk, Label, Entry, Button
from tkinter.ttk import Notebook, Frame, Treeview
from controller import user_controller, product_controller, sale_controller

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
        
        self.sale_tab()
        
        self.cart = dict()
        
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
        
        self.user_treeview = Treeview(body_frame, columns=("Nombre", "Apellidos", "Usuario"))
        self.user_treeview.pack(fill="x", expand=True)
        self.user_treeview.heading("#0", text="ID")
        self.user_treeview.heading("#1", text="Nombre")
        self.user_treeview.heading("#2", text="Apellidos")
        self.user_treeview.heading("#3", text="Usuario")

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
        
        self.product_treeview = Treeview(body_frame, columns=("Nombre", "Descripción", "Precio", "Stock"))
        self.product_treeview.pack(fill="x", expand=True)
        self.product_treeview.heading("#0", text="ID")
        self.product_treeview.heading("#1", text="Nombre")
        self.product_treeview.heading("#2", text="Descripción")
        self.product_treeview.heading("#3", text="Precio")
        self.product_treeview.heading("#4", text="Stock")
        
    def sale_tab(self):
        tab1 = Frame(self.notebook)
        self.notebook.add(tab1, text = "Ventas")
        
        head_frame = Frame(tab1)
        head_frame.pack(fill="x", expand=True, pady=10, padx=10)
        
        head_frame_left = Frame(head_frame)
        head_frame_left.pack(side="left", padx=5)
        
        self.label_creator(head_frame_left, "Producto", 0, 0)
        self.product_entry = self.entry_creator(head_frame_left, 1, 0)
        
        self.label_creator(head_frame_left, "Cantidad", 0, 1)
        self.quantity_entry = self.entry_creator(head_frame_left, 1, 1)
        
        add_button = Button(head_frame_left, text="Agregar", command=self.add_to_cart)
        add_button.grid(row=2, columnspan=2, pady=10)
        
        head_frame_right = Frame(head_frame)
        head_frame_right.pack(side="right", padx=5)
        
        self.billing_treeview = Treeview(head_frame_right, columns=("Concepto", "Precio unitario", "Cantidad", "Total parcial"))
        self.billing_treeview.pack(fill="x", expand=True)
        self.billing_treeview.heading("#0", text="ID")
        self.billing_treeview.heading("#1", text="Concepto")
        self.billing_treeview.heading("#2", text="Precio unitario")
        self.billing_treeview.heading("#3", text="Cantidad")
        self.billing_treeview.heading("#4", text="Total parcial")
        
        self.total_label = Label(head_frame_right, text="Total: 0 XAF", font=(14))
        self.total_label.pack()
        
        # save_button = Button(head_frame_right, text="Guardar", command=self.create_product)
        # save_button.grid(row=4, columnspan=2, pady=10)
        
        body_frame = Frame(tab1)
        body_frame.pack(fill="x", expand=True, padx=10)
        
        self.sale_treeview = Treeview(body_frame, columns=("Usuario", "Producto", "Cantidad", "Fecha"))
        self.sale_treeview.pack(fill="x", expand=True)
        self.sale_treeview.heading("#0", text="ID")
        self.sale_treeview.heading("#1", text="Usuario")
        self.sale_treeview.heading("#2", text="Producto")
        self.sale_treeview.heading("#3", text="Cantidad")
        self.sale_treeview.heading("#4", text="Fecha")
    
    def create_user(self):
        controller = user_controller.UserController()
        if controller.create(self.name_entry.get(), self.lastname_entry.get(), self.username_entry.get(), self.password_entry.get()):
            self.name_entry.delete(0, "end")
            self.lastname_entry.delete(0, "end")
            self.username_entry.delete(0, "end")
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
        for registro in self.user_treeview.get_children():
            self.user_treeview.delete(registro)
        
        for registro in controller.read():
            self.user_treeview.insert("", "end", text=registro[0], values=registro[1:])
    
    def read_products(self):
        controller = product_controller.ProductController()
        for registro in self.product_treeview.get_children():
            self.product_treeview.delete(registro)
        
        for registro in controller.read():
            self.product_treeview.insert("", "end", text=registro[0], values=registro[1:])
            
    def add_to_cart(self):
        controller = product_controller.ProductController()
        product = controller.add_to_cart(self.product_entry.get(), self.quantity_entry.get())
        
        if product:
            self.cart[product[0]] = product
            self.product_entry.delete(0, "end")
            self.quantity_entry.delete(0, "end")
            
        for registro in self.billing_treeview.get_children():
            self.billing_treeview.delete(registro)
        
        for key, value in self.cart.items():
            self.billing_treeview.insert("", "end", text=key, values=value[1:])
            self.total_label.config(text=f"Total: {int(value[2]) * int(value[3])}")

    
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