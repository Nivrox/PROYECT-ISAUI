import tkinter as tk
from tkinter import ttk, messagebox

from matplotlib import style
from servicio.cliente_servicio import ClienteServicio


class FormularioClientes():

    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Clientes")
        self.master.geometry("1250x450")
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.cliente_servicio = ClienteServicio()
        self.id_seleccionado = None

        self.crear_componentes()
        self.cargar_datos()

    def crear_componentes(self):
        frame_form = tk.LabelFrame(self.master, text="Datos de Cliente")
        frame_form.pack(fill="x", padx=10, pady=10)
        frame_botones = tk.Frame(frame_form)
        frame_botones.grid(row=4, column=0, columnspan=4, pady=10)

        frame_izq = tk.Frame(frame_form)
        frame_izq.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

        frame_der = tk.Frame(frame_form)
        frame_der.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
    

        vcmd_dni = (self.master.register(self.valida_dni), '%P')
        tk.Label(frame_form, text="DNI").grid(row=0, column=0)
        self.entry_dni = tk.Entry(frame_form, validate="key", validatecommand=vcmd_dni)
        self.entry_dni.grid(row=0, column=1, sticky="ew")

        vcmd_nombres = (self.master.register(self.validar_nombres), '%P')
        tk.Label(frame_form, text="Nombres").grid(row=1, column=0)
        self.entry_nombres = tk.Entry(frame_form, validate="key", validatecommand=vcmd_nombres)
        self.entry_nombres.grid(row=1, column=1, sticky="ew")


        tk.Label(frame_form, text="Apellidos").grid(row=2, column=0)
        vcmd_apellidos = (self.master.register(self.validar_apellidos), '%P')
        self.entry_apellidos = tk.Entry(frame_form, validate="key", validatecommand=vcmd_apellidos)
        self.entry_apellidos.grid(row=2, column=1, sticky="ew")

        tk.Label(frame_form, text="Sexo").grid(row=3, column=0)
        self.combo_sexo = ttk.Combobox(frame_form, values=["Masculino", "Femenino", "Otro"], state="readonly")
        self.combo_sexo.grid(row=3, column=1, sticky="ew")
        self.combo_sexo.current(0)

        tk.Label(frame_form, text="Estado").grid(row=3, column=2)
        self.combo_estado = ttk.Combobox(frame_form, values=["Activo", "Inactivo"], state="readonly")
        self.combo_estado.grid(row=3, column=3, sticky="ew")
        self.combo_estado.current(0)

        tk.Button(frame_botones, text="Guardar", width=12, command=self.guardar).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Modificar", width=12, command=self.modificar).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Eliminar", width=12, command=self.eliminar).grid(row=0, column=2, padx=5)
        tk.Button(frame_botones, text="Volver", width=12, command=self.master.destroy).grid(row=0, column=3, padx=5)
        
        frame_tabla = tk.Frame(self.master)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(
            frame_tabla,
            columns=("ID", "DNI", "Nombres", "Apellidos", "Sexo", "Estado"),
            show="headings"
        )

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)

        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar)

    def cargar_datos(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        clientes = self.cliente_servicio.listar_clientes()

        for cliente in clientes:
            self.tree.insert("", "end", values=(
                cliente.id_cliente,
                cliente.dni,
                cliente.nombres,
                cliente.apellidos,
                cliente.sexo,
                cliente.estado
            ))

    def seleccionar(self, event):
        seleccion = self.tree.focus()
        if seleccion:
            valores = self.tree.item(seleccion)["values"]
            self.id_seleccionado = valores[0]

            self.entry_dni.delete(0, tk.END)
            self.entry_dni.insert(0, valores[1])

            self.entry_nombres.delete(0, tk.END)
            self.entry_nombres.insert(0, valores[2])

            self.entry_apellidos.delete(0, tk.END)
            self.entry_apellidos.insert(0, valores[3])
            self.combo_sexo.set(valores[4])
            self.combo_estado.set(valores[5])

    def guardar(self):
        try:
            self.cliente_servicio.crear_cliente(
                self.entry_dni.get(),
                self.entry_nombres.get(),
                self.entry_apellidos.get(),
                self.combo_sexo.get(),
                self.combo_estado.get()
            )
            self.cargar_datos()
            self.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def modificar(self):
        if self.id_seleccionado is None:
            messagebox.showwarning("Advertencia", "Seleccione un registro")
            return

        try:
            self.cliente_servicio.actualizar_cliente(
                self.id_seleccionado,
                self.entry_dni.get(),
                self.entry_nombres.get(),
                self.entry_apellidos.get(),
                self.combo_sexo.get(),
                self.combo_estado.get()
            )
            self.cargar_datos()
            self.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar(self):
        if self.id_seleccionado is None:
            messagebox.showwarning("Advertencia", "Seleccione un registro")
            return

        self.cliente_servicio.eliminar_cliente(self.id_seleccionado)
        self.cargar_datos()
        self.limpiar_campos()

    def limpiar_campos(self):
        self.entry_dni.delete(0, tk.END)
        self.entry_nombres.delete(0, tk.END)
        self.entry_apellidos.delete(0, tk.END)
        self.combo_sexo.current(0)
        self.combo_estado.current(0)
        self.id_seleccionado = None
    
    def valida_dni(self,valor):
        if valor.isdigit() and len(valor) <= 8:
            return True
        if valor == "":
            return True
        return False
    
    def validar_nombres(self,valor):
        if valor == "":
            return True
        if len(valor) > 24: 
            return False
        if all(c.isalpha() or c.isspace() for c in valor):
            return True
        return False
    
    def validar_apellidos(self,valor):
        if valor == "":
            return True
        if len(valor) > 18: 
            return False
        if all(c.isalpha() or c.isspace() for c in valor):
            return True
        return False