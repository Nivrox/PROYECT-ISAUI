import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry  # Importamos DateEntry para el calendario
import mysql.connector  # Asegúrate de que tienes esta biblioteca
from ConexionBDBiblioteca import conexion  # Importa la función de conexión a la BD

def prestamos_interface():
    root = tk.Tk()
    root.title("Gestión de Préstamos - Biblioteca José H. Porto")
    
    # Definir tamaño fijo y que no se pueda cambiar
    root.geometry("780x680+100+40")
    root.resizable(True, True)
    root.configure(bg="#5271ff")  # Cambiado a blanco

    # Crear un marco con dos colores divididos
    marco_dividido = tk.Frame(root, bd=5, relief=tk.RAISED, bg="#231c00")  # Marco en gris claro
    marco_dividido.grid(row=0, column=0, columnspan=2, pady=0, sticky='ew', padx=(35,10))

    # Color superior
    top_color = tk.Label(marco_dividido, bg="#fef0b1", height=3)
    top_color.pack(side=tk.TOP, fill=tk.X)

    # Color inferior
    bottom_color = tk.Label(marco_dividido, bg="#000000", height=3)
    bottom_color.pack(side=tk.BOTTOM, fill=tk.X)

    # Título centrado en el marco
    tk.Label(marco_dividido, text="Gestión de Préstamos", font=("Arial", 24), fg="black", bg="white").place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Campo de búsqueda de socio
    tk.Label(root, text="Buscar Socio (por DNI, Nombre o Apellido):", font=("Arial", 14), bg="white", fg="black").grid(row=1, column=0, sticky='e', padx=10, pady=10)
    search_entry = tk.Entry(root, font=("Arial", 14), width=30)
    search_entry.grid(row=1, column=1, sticky='w', padx=10)

    # Crear el Combobox para mostrar los resultados de búsqueda
    socio_combobox = ttk.Combobox(root, font=("Arial", 14), width=40)
    socio_combobox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Función para buscar socio en la base de datos
    def buscar_socio():
        dni_nombre_apellido_busqueda = search_entry.get().strip()

        try:
            mycursor, mydb = conexion()

            # Buscar socio por DNI, Nombre o Apellido
            sql = """
                SELECT DNI, Nombre, Apellido 
                FROM socios 
                WHERE DNI LIKE %s OR Nombre LIKE %s OR Apellido LIKE %s
            """
            mycursor.execute(sql, (f"%{dni_nombre_apellido_busqueda}%", f"%{dni_nombre_apellido_busqueda}%", f"%{dni_nombre_apellido_busqueda}%"))
            resultado = mycursor.fetchall()

            # Limpiar el combobox antes de agregar nuevos valores
            socio_combobox['values'] = []

            if resultado:
                # Formatear los resultados como "DNI - Nombre Apellido" para el combobox
                socios = [f"{socio[0]} - {socio[1]} {socio[2]}" for socio in resultado]
                socio_combobox['values'] = socios
                socio_combobox.current(0)  # Seleccionar el primer resultado
            else:
                messagebox.showinfo("Buscar", f"No se encontró ningún socio con el criterio: {dni_nombre_apellido_busqueda}")
            
            mycursor.close()
            mydb.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error en la búsqueda: {err}")

    # Función para buscar libros en la base de datos mientras el usuario escribe
    def buscar_libros_event(event=None):
        buscar_libros()

    def buscar_libros():
        nombre_libro = libro_search_entry.get().strip()
        if not nombre_libro:
            libro_combobox['values'] = []  # Limpiar combobox si no hay texto
            return

        try:
            mycursor, mydb = conexion()

            sql = "SELECT titulo, num_ejemplar FROM libros WHERE titulo LIKE %s"
            mycursor.execute(sql, (f"%{nombre_libro}%",))
            resultado = mycursor.fetchall()

            libro_combobox['values'] = []  # Limpiar valores anteriores
            if resultado:
                libros = [f"{titulo} - {num_ejemplar}" for titulo, num_ejemplar in resultado]
                libro_combobox['values'] = libros  # Actualizar valores del combobox
                libro_combobox.event_generate('<Down>')  # Despliega el combobox automáticamente
            else:
                libro_combobox['values'] = []

            mycursor.close()
            mydb.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error en la búsqueda de libros: {err}")

    # Función para registrar el préstamo del socio seleccionado
    def registrar_prestamo():
        socio_seleccionado = socio_combobox.get()
        if socio_seleccionado:
            fecha_prestamo = date_entry.get()  # Obtener la fecha seleccionada
            fecha_devolucion = devolucion_entry.get()  # Obtener la fecha de devolución seleccionada
            libro_seleccionado = libro_combobox.get()  # Obtener el libro seleccionado

            if libro_seleccionado:
                try:
                    libro_titulo, libro_edicion = libro_seleccionado.split(" - ")

                    mycursor, mydb = conexion()

                    # Extraer el DNI del socio seleccionado
                    dni_socio = socio_seleccionado.split(" - ")[0]

                    # Buscar el ID del socio en la base de datos (por su DNI)
                    sql_socio = "SELECT id_socios FROM socios WHERE DNI = %s"
                    mycursor.execute(sql_socio, (dni_socio,))
                    id_socio = mycursor.fetchone()[0]

                    # Buscar el ID del libro en la base de datos (por su título y edición)
                    sql_libro = "SELECT id_libros FROM libros WHERE titulo = %s AND num_ejemplar = %s"
                    mycursor.execute(sql_libro, (libro_titulo.strip(), libro_edicion.strip()))
                    id_libro = mycursor.fetchone()[0]

                    # Registrar el préstamo
                    sql_prestamo = """
                        INSERT INTO prestamos (id_socios, id_libros, fecha_prestamo, fecha_devolucion, estado_prestamo)
                        VALUES (%s, %s, %s, %s, %s)
                    """
                    valores = (id_socio, id_libro, fecha_prestamo, fecha_devolucion, 'Pendiente')
                    mycursor.execute(sql_prestamo, valores)

                    # Confirmar la transacción
                    mydb.commit()

                    messagebox.showinfo("Préstamo Registrado", "El préstamo ha sido registrado exitosamente.")

                    mycursor.close()
                    mydb.close()

                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Error al registrar el préstamo: {err}")
            else:
                messagebox.showwarning("Error", "Debe seleccionar un libro.")
        else:
            messagebox.showwarning("Error", "No se ha seleccionado ningún socio.")

    # Función para cancelar y cerrar la ventana
    def cancelar():
        if messagebox.askyesno("Cancelar", "¿Estás seguro de que deseas cancelar y salir?"):
            root.destroy()  # Cerrar la ventana actual

    # Botón de búsqueda
    tk.Button(root, text="Buscar", font=("Arial", 14), command=buscar_socio).grid(row=1, column=1, sticky='e', padx=(0,10), pady=10)

    # Botón de cancelar
    tk.Button(root, text="Cancelar", font=("Arial", 14), command=cancelar, bg="red", fg="white").grid(row=8, column=0, columnspan=2, pady=10)

    # Campo de búsqueda de libros
    tk.Label(root, text="Buscar Libro (por título):", font=("Arial", 14), bg="white", fg="black").grid(row=3, column=0, sticky='e', padx=10, pady=10)
    libro_search_entry = tk.Entry(root, font=("Arial", 14), width=30)
    libro_search_entry.grid(row=3, column=1, sticky='w', padx=10)
    libro_search_entry.bind("<KeyRelease>", buscar_libros_event)  # Ejecuta búsqueda con cada tecla presionada

    libro_combobox = ttk.Combobox(root, font=("Arial", 14), width=28)
    libro_combobox.grid(row=6, column=1, padx=10, pady=10, sticky='w')

    # Campo de selección de la fecha de préstamo
    tk.Label(root, text="Fecha de Préstamo:", font=("Arial", 14), bg="white", fg="black").grid(row=4, column=0, sticky='e', padx=10, pady=10)
    date_entry = DateEntry(root, width=20, font=("Arial", 13), background='lightgreen', foreground='black', borderwidth=2, fieldbackground='lightyellow', locale= "es")
    date_entry.grid(row=4, column=1, sticky='w', padx=10)

    # Campo de selección de la fecha de devolución
    tk.Label(root, text="Fecha de Devolución:", font=("Arial", 14), bg="white", fg="black").grid(row=5, column=0, sticky='e', padx=10, pady=10)
    devolucion_entry = DateEntry(root, width=20, font=("Arial", 13), background='lightgreen', foreground='black', borderwidth=2, fieldbackground='lightyellow', locale= "es")
    devolucion_entry.grid(row=5, column=1, sticky='w', padx=10)

    # Botón para registrar el préstamo
    tk.Button(root, text="Registrar Préstamo", font=("Arial", 14), bg="lightgreen", command=registrar_prestamo).grid(row=7, column=0, columnspan=2, pady=20)

    root.mainloop()

prestamos_interface()
