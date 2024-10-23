import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry  # Importamos DateEntry para el calendario
import mysql.connector  # Asegúrate de que tienes esta biblioteca
from ConexionBDBiblioteca import conexion  # Importa la función de conexión a la BD

def prestamos_interface():
    
    root = tk.Tk()
    root.title("Nuevo Préstamo")
    
    # Dimensiones fijas de la ventana
    root.geometry("350x700+500+70")
    root.configure(bg="#ff5100")  # Fondo naranja

    # Marco superior para el título con dos colores
    marco_titulo = tk.Frame(root, bg="#231c00", height=80)
    marco_titulo.pack(fill="x")

    # Etiqueta para "NUEVO"
    tk.Label(marco_titulo, text="NUEVO", font=("Arial", 18, "bold"), fg="white", bg="#231c00").place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    # Etiqueta para "PRESTAMO" (con color de fondo beige claro)
    tk.Label(marco_titulo, text="PRESTAMO", font=("Arial", 16, "bold"), fg="white", bg="#d9b38c").place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    # Función para buscar socio en la base de datos
    def buscar_socio():
        dni_busqueda = dni_entry.get().strip()

        try:
            mycursor, mydb = conexion()

            # Buscar socio por DNI
            sql = "SELECT Nombre, Apellido FROM socios WHERE DNI = %s"
            mycursor.execute(sql, (dni_busqueda,))
            resultado = mycursor.fetchone()

            if resultado:
                nombre_completo_entry.delete(0, tk.END)
                nombre_completo_entry.insert(0, f"{resultado[0]} {resultado[1]}")  # Nombre y Apellido
            else:
                messagebox.showinfo("Buscar", f"No se encontró ningún socio con el DNI: {dni_busqueda}")

            mycursor.close()
            mydb.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error en la búsqueda: {err}")

    # Función para buscar libros en la base de datos
    def buscar_libros():
        titulo_libro = titulo_entry.get().strip()
        try:
            mycursor, mydb = conexion()

            sql = "SELECT id_editorial FROM libros WHERE titulo = %s"
            mycursor.execute(sql, (titulo_libro,))
            resultado = mycursor.fetchone()

            if resultado:
                autor_entry.delete(0, tk.END)
                autor_entry.insert(0, resultado[0])  # Autor
            else:
                messagebox.showinfo("Buscar", f"No se encontró ningún libro con el título: {titulo_libro}")

            mycursor.close()
            mydb.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error en la búsqueda de libros: {err}")

    # Función para registrar el préstamo en la base de datos
    def registrar_prestamo():
        socio = nombre_completo_entry.get().strip()
        dni = dni_entry.get().strip()
        titulo = titulo_entry.get().strip()
        autor = autor_entry.get().strip()
        fecha_prestamo = date_entry.get()
        fecha_devolucion = devolucion_entry.get()

        if socio and dni and titulo and autor and fecha_prestamo and fecha_devolucion:
            try:
                mycursor, mydb = conexion()

                # Buscar el ID del socio por DNI
                sql_socio = "SELECT id_socios FROM socios WHERE DNI = %s"
                mycursor.execute(sql_socio, (dni,))
                id_socio = mycursor.fetchone()

                if id_socio:
                    # Buscar el ID del libro por título
                    sql_libro = "SELECT id_libros FROM libros WHERE titulo = %s"
                    mycursor.execute(sql_libro, (titulo,))
                    id_libro = mycursor.fetchone()

                    if id_libro:
                        # Registrar el préstamo
                        sql_prestamo = """
                            INSERT INTO prestamos (id_socios, id_libros, fecha_prestamo, fecha_devolucion, estado_prestamo)
                            VALUES (%s, %s, %s, %s, %s)
                        """
                        valores = (id_socio[0], id_libro[0], fecha_prestamo, fecha_devolucion, 'Pendiente')
                        mycursor.execute(sql_prestamo, valores)
                        mydb.commit()

                        messagebox.showinfo("Éxito", "El préstamo ha sido registrado exitosamente.")
                    else:
                        messagebox.showwarning("Error", "No se encontró el libro.")
                else:
                    messagebox.showwarning("Error", "No se encontró el socio.")

                mycursor.close()
                mydb.close()

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error al registrar el préstamo: {err}")
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")

    # Crear los campos y etiquetas para el formulario
    tk.Label(root, text="Nombre completo", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    nombre_completo_entry = tk.Entry(root, font=("Arial", 12), width=25)
    nombre_completo_entry.pack()

    tk.Label(root, text="DNI", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    dni_entry = tk.Entry(root, font=("Arial", 12), width=25)
    dni_entry.pack()

    tk.Button(root, text="Buscar Socio", font=("Arial", 10, "bold"), bg="#d9b38c", command=buscar_socio).pack(pady=10)

    tk.Label(root, text="Título", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    titulo_entry = tk.Entry(root, font=("Arial", 12), width=25)
    titulo_entry.pack()

    tk.Button(root, text="Buscar Libro", font=("Arial", 10, "bold"), bg="#d9b38c", command=buscar_libros).pack(pady=10)

    tk.Label(root, text="Autor", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    autor_entry = tk.Entry(root, font=("Arial", 12), width=25)
    autor_entry.pack()

    tk.Label(root, text="Fecha Préstamo", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    date_entry = DateEntry(root, font=("Arial", 12), width=23, background="lightgreen", foreground="black", borderwidth=2)
    date_entry.pack(pady=5)

    tk.Label(root, text="Fecha Devolución", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    devolucion_entry = DateEntry(root, font=("Arial", 12), width=23, background="lightgreen", foreground="black", borderwidth=2)
    devolucion_entry.pack(pady=5)

    # Botón para registrar el préstamo
    tk.Button(root, text="Registrar", font=("Arial", 12, "bold"), bg="#d9b38c", fg="black", command=registrar_prestamo).pack(pady=20)

    root.mainloop()

prestamos_interface()
