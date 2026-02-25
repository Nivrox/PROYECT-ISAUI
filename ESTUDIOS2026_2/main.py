import tkinter as tk
from tkinter import messagebox
from interfaz.formulario_personas import FormularioPersonas
from interfaz.formulario_clientes import FormularioClientes

class MenuPrincipal():

    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Gestión")
        self.master.geometry("400x200")

        tk.Label(master, text="Sistema ABM", font=("Arial", 16)).pack(pady=20)

        tk.Button(master, text="Gestión de Personas", width=25, command=self.abrir_personas).pack(pady=5)
        tk.Button(master, text="Gestión de Clientes", width=25, command=self.abrir_clientes).pack(pady=5)

    def abrir_personas(self):
        try:
            ventana = tk.Toplevel(self.master)
            FormularioPersonas(ventana)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def abrir_clientes(self):
        try: 
            ventana = tk.Toplevel(self.master)
            FormularioClientes(ventana)
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = MenuPrincipal(root)
    root.mainloop()
