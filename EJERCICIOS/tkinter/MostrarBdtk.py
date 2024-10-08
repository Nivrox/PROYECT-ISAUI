import tkinter as tk
from tkinter import ttk
import mysql.connector

# Conexión a la base de datos (reemplaza con tus datos)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",  # PONER SU PROPIO USUARIO
    password="bru455no",  # PONER SU PROPIA CLAVE
    database="isaui"
)
mycursor = mydb.cursor()

root = tk.Tk()
root.title("Listado de personas")

style = ttk.Style()  # crear objeto ttk.Style
style.configure("BigFont.TRadiobutton", font=("Helvetica", 14))  # configurar estilo de fuente

label_seleccionar_carrera = ttk.Label(root, text="Seleccionar carrera para filtrar", font=("Calibri", 20, "bold"))
label_seleccionar_carrera.grid(row=0, column=0, sticky="nsew", pady=(10, 0))

frame_superior = tk.Frame(root, bg="gray90")
frame_superior.grid(row=1, column=0, sticky="nsew")

frame_inferior = tk.Frame(root, bg="gray90")
frame_inferior.grid(row=2, column=0, sticky="nsew")

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)

# Configuración de los botones
variable_de_filtro_carrera = tk.StringVar()

frame_superior.rowconfigure(0, weight=1)
frame_superior.rowconfigure(1, weight=1)
frame_superior.columnconfigure(0, weight=1)
frame_superior.columnconfigure(1, weight=1)
frame_superior.columnconfigure(2, weight=1)

# Opciones de carreras para filtrar
for i, carrera in enumerate(["Guía de Turismo", "Técnico en Turismo", "Trekking", "Software", "Enfermería", "Espacio"]):
    filtro_carrera = ttk.Radiobutton(frame_superior, text=carrera, variable=variable_de_filtro_carrera, value=carrera, style="BigFont.TRadiobutton")
    row = i // 3  # calculate row index
    col = i % 3  # calculate column index
    filtro_carrera.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)  # grid configuration

# Tabla para mostrar los registros
arbol = ttk.Treeview(frame_inferior, columns=("apellido", "nombre", "dni", "carrera"), show="headings")
arbol.grid(row=0, column=0, sticky="nsew")

arbol.heading("apellido", text="Apellido")
arbol.heading("nombre", text="Nombre")
arbol.heading("dni", text="DNI")
arbol.heading("carrera", text="Carrera")

# Función para mostrar los registros
def mostrar_registros():
    # Eliminar datos previos en la tabla
    for row in arbol.get_children():
        arbol.delete(row)
    
    carrera_seleccionada = variable_de_filtro_carrera.get()  # Obtener la carrera seleccionada
    if carrera_seleccionada:
        # Consulta SQL para obtener los registros filtrados por carrera
        query = "SELECT apellido, nombre, dni, id_carreras FROM personas WHERE id_carreras = %s"
        mycursor.execute(query, (carrera_seleccionada,))
    else:
        # Consulta SQL para obtener todos los registros si no se selecciona una carrera
        query = "SELECT apellido, nombre, dni, id_carreras FROM personas"
        mycursor.execute(query)
    
    # Insertar los resultados en la tabla
    for (apellido, nombre, dni, carrera) in mycursor:
        arbol.insert("", "end", values=(apellido, nombre, dni, carrera))

# Botón para ejecutar el filtro
btn_filtrar = ttk.Button(root, text="Filtrar", command=mostrar_registros)
btn_filtrar.grid(row=3, column=0, pady=10)

root.mainloop()