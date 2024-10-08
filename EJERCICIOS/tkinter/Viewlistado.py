import tkinter as tk
from tkinter import ttk
from ConexionBD import *

def abrir_ventana_listado():
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
        for row in arbol.get_children():
            arbol.delete(row)

        carrera_seleccionada = variable_de_filtro_carrera.get()
        print("Carrera seleccionada:", carrera_seleccionada)  # Para verificar qué valor se está utilizando

        if carrera_seleccionada == '7':  # Si se selecciona "Todas"
            consulta = """
                SELECT p.apellido, p.nombre, p.dni, c.nombre 
                FROM personas p
                JOIN carreras c ON p.id_carreras = c.id_carreras
            """
            mycursor.execute(consulta)
        else:
            consulta = """
                SELECT p.apellido, p.nombre, p.dni, c.nombre 
                FROM personas p
                JOIN carreras c ON p.id_carreras = c.id_carreras
                WHERE p.id_carreras = %s
            """
            mycursor.execute(consulta, (carrera_seleccionada,))

        for (apellido, nombre, dni, nombre_carrera) in mycursor:
            arbol.insert("", "end", values=(apellido, nombre, dni, nombre_carrera))

    variable_de_filtro_carrera = tk.StringVar(value='7')  # Valor por defecto para mostrar todas las carreras

    carreras = {
        1: "Software",
        2: "Enfermería",
        3: "Diseño de Espacios",
        4: "Guía de Trekking",
        5: "Guía de Turismo",
        6: "Turismo y Hotelería",
        7: "Todas"
    }

    for i, (id_carrera, nombre_carrera) in enumerate(carreras.items()):
        filtro_carrera = ttk.Radiobutton(frame_superior, text=nombre_carrera, variable=variable_de_filtro_carrera, value=str(id_carrera), style="BigFont.TRadiobutton", command=mostrar_registros)
        row = i // 3  # calcular el índice de fila
        col = i % 3  # calcular el índice de columna
        filtro_carrera.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)  # configuración de grid

    btn_cerrar = tk.Button(frame_inferior, text="Cerrar", command=root.destroy, font=('Calibri', 15), bg="#F8F8FF", width=10)
    btn_cerrar.grid(row=3, column=3, rowspan=2, padx=10, pady=10, sticky="nsew")

    mostrar_registros()

    root.mainloop()