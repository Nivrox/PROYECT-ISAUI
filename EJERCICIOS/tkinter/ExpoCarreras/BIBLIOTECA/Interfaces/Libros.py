import tkinter as tk
from tkinter import ttk

# Función para actualizar las subcategorías basadas en la categoría seleccionada
def actualizar_subcategorias(event):
    categoria = categoria_var.get()
    subcategorias = []
    
    if categoria == "Novela":
        subcategorias = ["Novela histórica", "Novela contemporánea", "Ciencia ficción"]
    elif categoria == "Salud":
        subcategorias = ["Nutrición", "Ejercicio", "Medicina"]
    elif categoria == "Tecnología":
        subcategorias = ["Inteligencia Artificial", "Redes", "Desarrollo de Software"]
    
    desplegable_subcategoria['values'] = subcategorias
    subcategoria_var.set('')  # Reiniciar selección de subcategoría
    desplegable_subcategoria.grid(row=4, column=1, padx=10, pady=5)  # Mostrar subcategoría después de seleccionar una categoría

# Función para agregar un libro a la tabla
def agregar_libro():
    titulo = entrada_titulo.get()
    autor = entrada_autor.get()
    editorial = entrada_editorial.get()  # Obtener el valor de la editorial
    categoria = categoria_var.get()
    subcategoria = subcategoria_var.get()
    descripcion = entrada_descripcion.get("1.0", tk.END).strip()  # Obtener texto completo de la descripción
    isbn = entrada_isbn.get()
    
    if titulo and autor and editorial and categoria and subcategoria and descripcion and isbn:
        tabla_libros.insert("", "end", values=(isbn, titulo, categoria, subcategoria, autor, editorial, descripcion))
        limpiar_campos()

# Función para limpiar los campos de entrada
def limpiar_campos():
    entrada_titulo.delete(0, tk.END)
    entrada_autor.delete(0, tk.END)
    entrada_editorial.delete(0, tk.END)  # Limpiar el campo de editorial
    entrada_isbn.delete(0, tk.END)
    entrada_descripcion.delete("1.0", tk.END)
    categoria_var.set('')
    subcategoria_var.set('')
    desplegable_subcategoria.grid_forget()  # Ocultar el campo de subcategoría hasta que se seleccione una categoría

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de Biblioteca")
root.geometry("800x600")

# Tabla para mostrar los libros
columnas = ("ISBN", "Título", "Categoría", "Subcategoría", "Autor", "Editorial", "Descripción")
tabla_libros = ttk.Treeview(root, columns=columnas, show="headings")
for col in columnas:
    tabla_libros.heading(col, text=col)
    tabla_libros.column(col, width=120)

tabla_libros.pack(fill=tk.BOTH, expand=True)

# Marco para los detalles del libro
frame = tk.Frame(root)
frame.pack(pady=10)

# Etiquetas y entradas para los detalles del libro
tk.Label(frame, text="Título:").grid(row=0, column=0, padx=10, pady=5)
entrada_titulo = tk.Entry(frame)
entrada_titulo.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Autor:").grid(row=1, column=0, padx=10, pady=5)
entrada_autor = tk.Entry(frame)
entrada_autor.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Editorial:").grid(row=2, column=0, padx=10, pady=5)  # Nueva etiqueta para la editorial
entrada_editorial = tk.Entry(frame)  # Nueva entrada para la editorial
entrada_editorial.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text="ISBN:").grid(row=3, column=0, padx=10, pady=5)
entrada_isbn = tk.Entry(frame)
entrada_isbn.grid(row=3, column=1, padx=10, pady=5)

tk.Label(frame, text="Categoría:").grid(row=4, column=0, padx=10, pady=5)
categoria_var = tk.StringVar()
desplegable_categoria = ttk.Combobox(frame, textvariable=categoria_var)
desplegable_categoria['values'] = ("Novela", "Salud", "Tecnología")  # Agrega más categorías según sea necesario
desplegable_categoria.grid(row=4, column=1, padx=10, pady=5)

# Dropdown de Subcategoría (se actualizará según la categoría seleccionada)
tk.Label(frame, text="Subcategoría:").grid(row=5, column=0, padx=10, pady=5)
subcategoria_var = tk.StringVar()
desplegable_subcategoria = ttk.Combobox(frame, textvariable=subcategoria_var)

# Cuando se selecciona una categoría, se actualizan las subcategorías
desplegable_categoria.bind("<<ComboboxSelected>>", actualizar_subcategorias)

# Etiqueta y campo de texto para la descripción
tk.Label(frame, text="Descripción:").grid(row=6, column=0, padx=10, pady=5)
entrada_descripcion = tk.Text(frame, height=4, width=30)
entrada_descripcion.grid(row=6, column=1, padx=10, pady=5)

# Botón para agregar libro
boton_agregar = tk.Button(frame, text="Agregar Libro", command=agregar_libro)
boton_agregar.grid(row=7, column=1, padx=10, pady=10)

# Botón para cerrar
boton_cerrar = tk.Button(root, text="Cerrar", command=root.quit)
boton_cerrar.pack(pady=10)

root.mainloop()
