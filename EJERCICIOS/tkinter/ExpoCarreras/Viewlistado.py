import tkinter as tk
from tkinter import ttk
from ConexionBD import *

def abrir_ventana_listado(datos):
    root = tk.Toplevel()
    root.title("Listado de personas")
   

    style = ttk.Style()
    style.configure("BigFont.TRadiobutton", font=("Helvetica", 14))

    label_seleccionar_carrera = tk.Label(root, text="Seleccionar carrera para filtrar",bg="#b39658", font=("Calibri", 20, "bold"))
    label_seleccionar_carrera.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=(10, 0))

    frame_superior = tk.Frame(root)
    frame_superior.grid(row=1, column=0, sticky="nsew", columnspan=3)  # Frame para los radio buttons

    frame_inferior = tk.Frame(root, bg="#dbc79c")
    frame_inferior.grid(row=2, column=0, columnspan=4, sticky="nsew")

    arbol = ttk.Treeview(frame_inferior, columns=("apellido", "nombre", "dni", "carrera"), show="headings")
    arbol.grid(row=0, column=0, columnspan=4, sticky="nsew")

    arbol.heading("apellido", text="Apellido")
    arbol.heading("nombre", text="Nombre")
    arbol.heading("dni", text="DNI")
    arbol.heading("carrera", text="Carrera")

    def mostrar_registros():

        
        for fila in datos:
            arbol.insert("", "end", values = fila)

        arbol.pack (padx= 20 , pady = 20)


    btn_cerrar = tk.Button(frame_inferior, text="Cerrar", command=root.destroy, font=('Calibri', 15), bg="#F8F8FF", width=10)
    btn_cerrar.grid(row=3, column=3, rowspan=2, padx=10, pady=10, sticky="nsew")

    mostrar_registros()

    root.mainloop()