import tkinter as tk
from tkinter import messagebox

def login_interface():
    root = tk.Tk()
    root.title("Iniciar Sesión - Biblioteca José H. Porto")
    root.geometry("1366x768")

    # Desactivar la opción de redimensionar la ventana
    root.resizable(False, False)

    # Etiqueta de título
    tk.Label(root, text="Iniciar Sesión", font=("Arial", 24)).pack(pady=30)

    # Campo de usuario
    tk.Label(root, text="Usuario:", font=("Arial", 14)).pack(pady=10)
    user_entry = tk.Entry(root, font=("Arial", 12))
    user_entry.pack()

    # Campo de contraseña
    tk.Label(root, text="Contraseña:", font=("Arial", 14)).pack(pady=10)
    pass_entry = tk.Entry(root, show="*", font=("Arial", 12))
    pass_entry.pack()

    # Mostrar/ocultar contraseña
    show_pass_var = tk.IntVar()
    def toggle_password():
        if show_pass_var.get():
            pass_entry.config(show="")
        else:
            pass_entry.config(show="*")

    tk.Checkbutton(root, text="Mostrar contraseña", variable=show_pass_var, command=toggle_password).pack(pady=10)

    # Función de inicio de sesión
    def iniciar_sesion():
        user = user_entry.get()
        password = pass_entry.get()

        # Validación de campos vacíos
        if not user or not password:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos")
            return
        
        # Lógica para verificar usuario y contraseña
        if user == "admin" and password == "1234":
            messagebox.showinfo("Login", "Inicio de sesión exitoso")
            root.destroy()  # Cerrar la ventana actual si el login es exitoso
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
                                                                                                                                                                                                   
    # Botón para iniciar sesión
    tk.Button(root, text="Iniciar Sesión", font=("Arial", 14), command=iniciar_sesion).pack(pady=20)
    def abrir_dashboard():
        abrir_dashboard
    root.mainloop()

if __name__ == "__main__":
    login_interface()