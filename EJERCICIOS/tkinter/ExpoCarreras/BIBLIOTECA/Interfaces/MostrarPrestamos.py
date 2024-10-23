import tkinter as tk
from tkinter import ttk
from ConexionBDBiblioteca import conectar  # Importa la función que conecta a la base de datos

def abrir_ventana_prestamos():
    root = tk.Tk()  # Si es la ventana principal, usa Tk en lugar de Toplevel
    root.title("Listado de Préstamos")

    style = ttk.Style()
    style.configure("BigFont.TRadiobutton", font=("Helvetica", 14))

    label_seleccionar_socio = tk.Label(root, text="Seleccionar socio para filtrar", bg="#b39658", font=("Calibri", 20, "bold"))
    label_seleccionar_socio.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=(10, 0))

    frame_superior = tk.Frame(root)
    frame_superior.grid(row=1, column=0, sticky="nsew", columnspan=3)  # Frame para los radio buttons

    frame_inferior = tk.Frame(root, bg="#dbc79c")
    frame_inferior.grid(row=2, column=0, columnspan=4, sticky="nsew")

    arbol = ttk.Treeview(frame_inferior, columns=("socios", "libro", "fecha_prestamo", "fecha_devolucion"), show="headings")
    arbol.grid(row=0, column=0, columnspan=4, sticky="nsew")

    arbol.heading("socios", text="Socio")
    arbol.heading("libro", text="Libro")
    arbol.heading("fecha_prestamo", text="Fecha de Préstamo")
    arbol.heading("fecha_devolucion", text="Fecha de Devolución")

    # Conectar a la base de datos
    conexion = conectar()
    cursor = conexion.cursor()

    def mostrar_prestamos():
        # Limpiar la tabla
        for row in arbol.get_children():
            arbol.delete(row)

        socio_seleccionado = variable_de_filtro_socio.get()
        print("Socio seleccionado:", socio_seleccionado)  # Para verificar qué valor se está utilizando

        if socio_seleccionado == '0':  # Si se selecciona "Todos"
            consulta = """
                SELECT CONCAT(s.apellido, ', ', s.nombre) AS socios, l.titulo, p.fecha_prestamo, p.fecha_devolucion, p.id_prestamos
                FROM prestamos p
                JOIN socios s ON p.id_socios = s.id_socios
                JOIN libros l ON p.id_libros = l.id_libros
            """
            cursor.execute(consulta)
        else:
            consulta = """
                SELECT CONCAT(s.apellido, ', ', s.nombre) AS socios, l.titulo, p.fecha_prestamo, p.fecha_devolucion, p.id_prestamos
                FROM prestamos p
                JOIN socios s ON p.id_socios = s.id_socios
                JOIN libros l ON p.id_libro = l.id_libro
                WHERE s.id_socios = %s
            """
            cursor.execute(consulta, (socio_seleccionado,))

        for (socio, libro, fecha_prestamo, fecha_devolucion, id_prestamo) in cursor:
            arbol.insert("", "end", values=(socio, libro, fecha_prestamo, fecha_devolucion, id_prestamo))

    def cargar_datos_seleccionados(event):
        # Obtener el ítem seleccionado
        seleccionado = arbol.selection()
        if seleccionado:
            item = arbol.item(seleccionado)
            valores = item['values']
            if valores:
                # Rellenar los campos de texto con los valores seleccionados
                entrada_socio.delete(0, tk.END)
                entrada_socio.insert(0, valores[0])  # Socio
                entrada_libro.delete(0, tk.END)
                entrada_libro.insert(0, valores[1])  # Libro
                entrada_fecha_prestamo.delete(0, tk.END)
                entrada_fecha_prestamo.insert(0, valores[2])  # Fecha préstamo
                entrada_fecha_devolucion.delete(0, tk.END)
                entrada_fecha_devolucion.insert(0, valores[3])  # Fecha devolución
                id_prestamo_seleccionado.set(valores[4])  # Guardar el id del préstamo seleccionado

    def actualizar_prestamo():
        # Obtener los datos de los campos
        socio = entrada_socio.get()
        libro = entrada_libro.get()
        fecha_prestamo = entrada_fecha_prestamo.get()
        fecha_devolucion = entrada_fecha_devolucion.get()
        id_prestamo = id_prestamo_seleccionado.get()

        # Actualizar en la base de datos
        consulta_actualizar = """
            UPDATE prestamos 
            SET fecha_prestamo = %s, fecha_devolucion = %s
            WHERE id_prestamos = %s
        """
        cursor.execute(consulta_actualizar, (fecha_prestamo, fecha_devolucion, id_prestamo))
        conexion.commit()

        # Refrescar la tabla después de actualizar
        mostrar_prestamos()

    def eliminar_prestamo():
        # Obtener el id del préstamo seleccionado
        id_prestamo = id_prestamo_seleccionado.get()

        if id_prestamo:
            # Eliminar de la base de datos
            consulta_eliminar = """
                DELETE FROM prestamos 
                WHERE id_prestamos = %s
            """
            cursor.execute(consulta_eliminar, (id_prestamo,))
            conexion.commit()

            # Refrescar la tabla después de eliminar
            mostrar_prestamos()

    # Crear campos para editar la información del préstamo seleccionado
    id_prestamo_seleccionado = tk.StringVar()  # Almacenar el id del préstamo seleccionado

    tk.Label(frame_inferior, text="Socio:").grid(row=1, column=0, padx=5, pady=5)
    entrada_socio = tk.Entry(frame_inferior)
    entrada_socio.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_inferior, text="Libro:").grid(row=2, column=0, padx=5, pady=5)
    entrada_libro = tk.Entry(frame_inferior)
    entrada_libro.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame_inferior, text="Fecha Préstamo:").grid(row=3, column=0, padx=5, pady=5)
    entrada_fecha_prestamo = tk.Entry(frame_inferior)
    entrada_fecha_prestamo.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(frame_inferior, text="Fecha Devolución:").grid(row=4, column=0, padx=5, pady=5)
    entrada_fecha_devolucion = tk.Entry(frame_inferior)
    entrada_fecha_devolucion.grid(row=4, column=1, padx=5, pady=5)

    # Botón para actualizar los datos
    btn_actualizar = tk.Button(frame_inferior, text="Actualizar", command=actualizar_prestamo)
    btn_actualizar.grid(row=5, column=0, columnspan=2, pady=10)

    # Botón para eliminar el préstamo seleccionado
    btn_eliminar = tk.Button(frame_inferior, text="Eliminar", command=eliminar_prestamo)
    btn_eliminar.grid(row=6, column=0, columnspan=2, pady=10)

    arbol.bind("<<TreeviewSelect>>", cargar_datos_seleccionados)

    variable_de_filtro_socio = tk.StringVar(value='0')  # Valor por defecto para mostrar todos los socios

    # Aquí puedes reemplazar estos valores con una consulta a la base de datos para obtener los socios
    socios = {
        0: "Todos",
        1: "Juan Pérez",
        2: "Ana Gómez",
        3: "Carlos López"
        # Agrega más socios según los datos de tu BD
    }

    for i, (id_socio, nombre_socio) in enumerate(socios.items()):
        filtro_socio = ttk.Radiobutton(frame_superior, text=nombre_socio, variable=variable_de_filtro_socio, value=str(id_socio), style="BigFont.TRadiobutton", command=mostrar_prestamos)
        row = i // 3  # calcular el índice de fila
        col = i % 3  # calcular el índice de columna
        filtro_socio.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)  # configuración de grid

    btn_cerrar = tk.Button(frame_inferior, text="Cerrar", command=root.destroy, font=('Calibri', 15), bg="#F8F8FF", width=10)
    btn_cerrar.grid(row=7, column=1, pady=10, sticky="nsew")

    mostrar_prestamos()

    root.mainloop()

# Ejecutar la función
if __name__ == "__main__":
    abrir_ventana_prestamos()
