import tkinter as tk
from tkinter import messagebox

def socios_interface():
    root = tk.Tk()
    root.title("Alta de Socio - Biblioteca José H. Porto")
    root.geometry("1366x768")

    # Desactivar la opción de redimensionar la ventana
    root.resizable(False, False)

    # Etiqueta de título
    tk.Label(root, text="Alta de Socio", font=("Arial", 24)).pack(pady=30)

    # Campos de entrada
    tk.Label(root, text="Nombre:", font=("Arial", 14)).pack(pady=10)
    nombre_entry = tk.Entry(root, font=("Arial", 12))
    nombre_entry.pack()

    tk.Label(root, text="Apellido:", font=("Arial", 14)).pack(pady=10)
    apellido_entry = tk.Entry(root, font=("Arial", 12))
    apellido_entry.pack()

    tk.Label(root, text="DNI:", font=("Arial", 14)).pack(pady=10)
    dni_entry = tk.Entry(root, font=("Arial", 12))
    dni_entry.pack()

    tk.Label(root, text="Fecha De Pago (dd/mm/aaaa):", font=("Arial", 14)).pack(pady=10)
    pago_entry = tk.Entry(root, font=("Arial", 12))
    pago_entry.pack()

    tk.Label(root, text="Monto ($):", font=("Arial", 14)).pack(pady=10)
    monto_entry = tk.Entry(root, font=("Arial", 12))
    monto_entry.pack()

    # Función para actualizar socio
    def actualizar_socio():
        nombre = nombre_entry.get()
        apellido = apellido_entry.get()
        dni = dni_entry.get()
        pago = pago_entry.get()
        monto = monto_entry.get()

        # Validación de campos vacíos
        if not nombre or not apellido or not dni or not pago or not monto:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
            return

        # Aquí iría la lógica para actualizar la información del socio
        messagebox.showinfo("Alta de Socio", f"Socio {nombre} {apellido} agregado exitosamente")

    # Botón para actualizar socio
    tk.Button(root, text="Agregar Socio", font=("Arial", 14), command=actualizar_socio).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    socios_interface()