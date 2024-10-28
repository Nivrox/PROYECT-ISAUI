import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import ttk

def mostrar_datos_en_grilla():
    try:
        # Conexión a la base de datos MySQL
        conexion = mysql.connector.connect(
            host='localhost',         # Cambia a tu host
            database='isaui',     # Nombre de la base de datos
            user='root',           # Usuario de MySQL
            password='nico455co'     # Contraseña del usuario
        )

        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")

            # Crear cursor para ejecutar consultas
            cursor = conexion.cursor()

            # Consulta para seleccionar los datos de la tabla
            consulta = "SELECT * FROM nombre_tabla;"  # Cambia 'nombre_tabla' por tu tabla
            cursor.execute(consulta)

            # Obtener todos los registros de la tabla
            registros = cursor.fetchall()

            # Crear ventana de Tkinter
            ventana = tk.Tk()
            ventana.title("Datos de la Base de Datos")

            # Crear Treeview (grilla)
            tree = ttk.Treeview(ventana)

            # Obtener el número de columnas de la tabla
            columnas = [desc[0] for desc in cursor.description]
            tree["columns"] = columnas

            # Configurar las columnas del Treeview
            for col in columnas:
                tree.heading(col, text=col)  # Encabezado
                tree.column(col, anchor=tk.CENTER)  # Centrar texto en la columna

            # Insertar los datos en el Treeview
            for fila in registros:
                tree.insert("", tk.END, values=fila)

            # Empaquetar el Treeview en la ventana
            tree.pack(expand=True, fill=tk.BOTH)

            # Iniciar la aplicación Tkinter
            ventana.mainloop()

    except Error as e:
        print("Error al conectar a MySQL:", e)

    finally:
        # Cerrar la conexión a la base de datos
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión a MySQL cerrada")