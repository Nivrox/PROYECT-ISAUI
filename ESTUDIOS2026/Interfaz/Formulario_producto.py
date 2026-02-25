import tkinter as tk
from tkinter import ttk, messagebox
from Servicios.Servicio_producto import ServicioProducto

class FormularioProducto:

    def __init__(self, root):
        self.root = root
        self.root.title("ABM Productos")

        self.crear_widgets()
        self.cargar_datos()

    def crear_widgets(self):
        tk.Label(self.root, text="Tipo").grid(row=0, column=0)
        self.combo_tipo = ttk.Combobox(self.root, values=["digital", "fisico"], state="readonly")
        self.combo_tipo.grid(row=0, column=1)

        tk.Label(self.root, text="Nombre").grid(row=1, column=0)
        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.grid(row=1, column=1)

        tk.Label(self.root, text="Precio").grid(row=2, column=0)
        self.entry_precio = tk.Entry(self.root)
        self.entry_precio.grid(row=2, column=1)

        tk.Label(self.root, text="Tamaño/Peso").grid(row=3, column=0)
        self.entry_atributo = tk.Entry(self.root)
        self.entry_atributo.grid(row=3, column=1)

        tk.Button(self.root, text="Guardar", command=self.guardar).grid(row=4, column=0)

        self.tree = ttk.Treeview(self.root, columns=("ID","Nombre","Precio","Tipo","Atributo"), show="headings")
        for col in ("ID","Nombre","Precio","Tipo","Atributo"):
            self.tree.heading(col, text=col)
        self.tree.grid(row=5, column=0, columnspan=2)

    def guardar(self):
        try:
            tipo = self.combo_tipo.get()
            nombre = self.entry_nombre.get()
            precio = self.entry_precio.get()
            atributo = self.entry_atributo.get()

            ServicioProducto.crear_producto(tipo, nombre, precio, atributo)
            messagebox.showinfo("Éxito", "Producto guardado")
            self.cargar_datos()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def cargar_datos(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        productos = ServicioProducto.obtener_productos()

        for p in productos:
            if p.obtener_tipo() == "digital":
                atributo = p.tamaño_archivo
            else:
                atributo = p.peso

            self.tree.insert("", tk.END, values=(
                p.id,
                p.nombre,
                p.precio,
                p.obtener_tipo(),
                atributo
            ))