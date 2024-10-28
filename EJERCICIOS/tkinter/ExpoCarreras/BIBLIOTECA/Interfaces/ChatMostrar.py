import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Función para crear la ventana y mostrar los datos en una grilla
def mostrar_datos(datos):
    # Crear la ventana
    ventana = tk.Tk()
    ventana.title("Datos de Socios")

    # Crear el Treeview para mostrar la información
    tree = ttk.Treeview(ventana, columns=("DNI", "Nombre", "Título del Libro", "Editorial", "Autor"), show="headings")

    # Definir los encabezados
    tree.heading("#1", text="DNI")
    tree.heading("#2", text="Nombre")
    tree.heading("#3", text="Título del Libro")
    tree.heading("#4", text="Editorial")
    tree.heading("#5", text="Autor")

    # Insertar los datos en el Treeview
    for fila in datos:
        tree.insert("", "end", values=fila)

    # Empaquetar el Treeview en la ventana
    tree.pack(padx=20, pady=20)

    # Botón para modificar la información seleccionada
    btn_modificar = tk.Button(ventana, text="Modificar", command=lambda: modificar_datos(tree))
    btn_modificar.pack(pady=5)

    # Botón para borrar la información seleccionada
    btn_borrar = tk.Button(ventana, text="Borrar", command=lambda: borrar_datos(tree))
    btn_borrar.pack(pady=5)

    # Iniciar el loop principal
    ventana.mainloop()

# Función para modificar datos (implementación a personalizar según necesidades)
def modificar_datos(tree):
    try:
        seleccionado = tree.selection()[0]  # Obtener el elemento seleccionado
        item = tree.item(seleccionado)
        datos = item['values']
        
        # Aquí puedes abrir otra ventana o cuadro de diálogo para editar los datos
        messagebox.showinfo("Modificar", f"Modificar datos de: {datos[1]}")  # Muestra el nombre como ejemplo

    except IndexError:
        messagebox.showwarning("Selección Inválida", "Por favor, seleccione un socio para modificar.")

# Función para borrar datos
def borrar_datos(tree):
    try:
        seleccionado = tree.selection()[0]  # Obtener el elemento seleccionado
        tree.delete(seleccionado)  # Borrar el elemento de la grilla
        messagebox.showinfo("Borrar", "Datos borrados exitosamente.")
        
        # Aquí puedes implementar la lógica para borrar los datos de la base de datos también

    except IndexError:
        messagebox.showwarning("Selección Inválida", "Por favor, seleccione un socio para borrar.")

# Ejemplo de uso con datos simulados
# Datos simulados de la consulta a MySQL (deberías reemplazarlos con los datos reales)
datos_socios = [
    ("12345678", "Juan Pérez", "El Gran Gatsby", "Editorial XYZ", "F. Scott Fitzgerald"),
    ("87654321", "Ana Gómez", "Cien años de soledad", "Editorial ABC", "Gabriel García Márquez"),
    ("23456789", "Luis Martínez", "1984", "Editorial 123", "George Orwell")
]

# Llamar a la función para mostrar los datos
mostrar_datos(datos_socios)