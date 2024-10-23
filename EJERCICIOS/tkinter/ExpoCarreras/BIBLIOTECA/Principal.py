from Interfaces import Dashboard  # Importamos la ventana del dashboard
import tkinter as tk
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Iniciar Sesión - Biblioteca José H. Porto")
        self.geometry("1366x768")
        self.resizable(False, False)
        self.login_interface()  # Mostramos primero la interfaz de login

    def login_interface(self):
        # Etiqueta de título
        tk.Label(self, text="Iniciar Sesión", font=("Arial", 24)).pack(pady=30)

        # Campo de usuario
        tk.Label(self, text="Usuario:", font=("Arial", 14)).pack(pady=10)
        self.user_entry = tk.Entry(self, font=("Arial", 12))
        self.user_entry.pack()

        # Campo de contraseña
        tk.Label(self, text="Contraseña:", font=("Arial", 14)).pack(pady=10)
        self.pass_entry = tk.Entry(self, show="*", font=("Arial", 12))
        self.pass_entry.pack()

        # Mostrar/ocultar contraseña
        self.show_pass_var = tk.IntVar()
        tk.Checkbutton(self, text="Mostrar contraseña", variable=self.show_pass_var, command=self.toggle_password).pack(pady=10)

        # Botón para iniciar sesión
        tk.Button(self, text="Iniciar Sesión", font=("Arial", 14), command=self.iniciar_sesion).pack(pady=20)

    def toggle_password(self):
        # Función para mostrar/ocultar la contraseña
        if self.show_pass_var.get():
            self.pass_entry.config(show="")
        else:
            self.pass_entry.config(show="*")

    def iniciar_sesion(self):
        user = self.user_entry.get()
        password = self.pass_entry.get()

        # Validación de campos vacíos
        if not user or not password:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos")
            return

        # Lógica para verificar usuario y contraseña
        if user == "admin" and password == "1234":
            messagebox.showinfo("Login", "Inicio de sesión exitoso")
            self.abrir_dashboard()  # Llamar al dashboard después de login exitoso
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def abrir_dashboard(self):
        self.destroy()  # Cerrar ventana de login
        dashboard_window = tk.Tk()  # Crear una nueva ventana de Tkinter
        Dashboard(dashboard_window)  # Abrir la ventana del dashboard dentro de la nueva ventana

if __name__ == "__main__":
    app = App()
    app.mainloop()
