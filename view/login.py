from tkinter import Tk, Frame, Label, PhotoImage, Entry, Button
from controller.user_controller import UserController
from view.dashboard import Dashboard

class Login(Tk):
    def __init__(self):
        super().__init__()
        self.title("Inicio de sesión")
        self.maxsize(300, 350)
        self.minsize(300, 350)
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        x = str(round((screen_width - 300) / 2))
        y = str(round((screen_height - 350) / 2))
        
        self.geometry(f"300x350+{x}+{y}")
        
        head_frame = Frame(self)
        head_frame.pack(fill="x")
        
        Label(head_frame, text="Inicio de Sesión", font=("Arial", 18)).pack(pady=20)
        
        user_image = PhotoImage(file="img/user.png")
        Label(head_frame, image=user_image, width=100, height=100).pack()
        
        body_frame = Frame(self)
        body_frame.pack(fill="x", padx=30)
        
        Label(body_frame, text="Usuario").grid(column=0, row=0, pady=10, sticky="w")
        self.username_entry = Entry(body_frame, width=35)
        self.username_entry.grid(column=1, row=0, pady=10, sticky="ns")
        
        Label(body_frame, text="Contraseña").grid(column=0, row=1, sticky="w")
        self.password_entry = Entry(body_frame, width=35, show="*")
        self.password_entry.grid(column=1, row=1, sticky="ns")
        
        footer_frame = Frame(self)
        footer_frame.pack(fill="x", pady=30)
        
        login_button = Button(footer_frame, text="Iniciar sesión", command=self.login)
        login_button.pack()
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user_controller = UserController()
        result = user_controller.login(username, password)
        if result:
            self.withdraw()
            dashboard = Dashboard()
            dashboard.deiconify()
            
