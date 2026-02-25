import tkinter as tk
from Interfaz.Formulario_producto import FormularioProducto

def iniciar():
    root = tk.Tk()
    app = FormularioProducto(root)
    root.mainloop()