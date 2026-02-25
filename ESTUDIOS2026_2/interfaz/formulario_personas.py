import tkinter as tk
from tkinter import ttk, messagebox
from servicio.persona_servicio import PersonaServicio


class FormularioPersonas():

    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Personas")
        self.master.geometry("1080x400")
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.persona_servicio = PersonaServicio()
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
        
        vdcmd_dni = (self.master.register(self.validar_dni), '%P')
        tk.Label(frame_izq, text="DNI").grid(row=0, column=0, sticky="w")
        self.entry_dni = tk.Entry(frame_izq, validate="key", validatecommand=vdcmd_dni)
        self.entry_dni.grid(row=0, column=1, sticky="ew")
        vdcmd_nombres = (self.master.register(self.validar_nombres), '%P')

        tk.Label(frame_izq, text="Nombres").grid(row=1, column=0, sticky="w")
        self.entry_nombres = tk.Entry(frame_izq, validate="key", validatecommand=vdcmd_nombres)
        self.entry_nombres.grid(row=1, column=1, sticky="ew")

        tk.Label(frame_izq, text="Apellidos").grid(row=2, column=0, sticky="w")
        vdcmd_apellidos = (self.master.register(self.validar_apellidos), '%P')
        self.entry_apellidos = tk.Entry(frame_izq, validate="key", validatecommand=vdcmd_apellidos)
        self.entry_apellidos.grid(row=2, column=1, sticky="ew")

        tk.Label(frame_izq, text="Sexo").grid(row=3, column=0, sticky="w")
        self.combo_sexo = ttk.Combobox(frame_izq, values=["Masculino", "Femenino", "Otro"], state="readonly")
        self.combo_sexo.grid(row=3, column=1, sticky="ew")
        self.combo_sexo.current(0)

        frame_botones = tk.Frame(frame_form)
        frame_botones.grid(row=4, column=0, columnspan=4, pady=10)

        tk.Button(frame_botones, text="Guardar", width=12, command=self.guardar).grid(row=0, column=0, padx=5, sticky="ew")
        tk.Button(frame_botones, text="Modificar", width=12, command=self.modificar).grid(row=0, column=1, padx=5, sticky="ew")
        tk.Button(frame_botones, text="Eliminar", width=12, command=self.eliminar).grid(row=0, column=2, padx=5, sticky="ew")
        tk.Button(frame_form, text="Volver", command=self.master.destroy).grid(row=4, column=4, padx=5, pady=5, sticky="ew") 
        
        frame_tabla = tk.Frame(self.master)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(
            frame_tabla,
            columns=("ID", "DNI", "Nombres", "Apellidos", "Sexo"),
            show="headings"
        )

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)

        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar)

    def cargar_datos(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        personas = self.persona_servicio.listar_personas()

        for persona in personas:
            self.tree.insert("", "end", values=(
                persona.id_persona,
                persona.dni,
                persona.nombres,
                persona.apellidos,
                persona.sexo
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

    def guardar(self):
        try:
            self.persona_servicio.crear_persona(
                self.entry_dni.get(),
                self.entry_nombres.get(),
                self.entry_apellidos.get(),
                self.combo_sexo.get()
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
            self.persona_servicio.actualizar_persona(
                self.id_seleccionado,
                self.entry_dni.get(),
                self.entry_nombres.get(),
                self.entry_apellidos.get(),
                self.combo_sexo.get()
            )
            self.cargar_datos()
            self.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar(self):
        if self.id_seleccionado is None:
            messagebox.showwarning("Advertencia", "Seleccione un registro")
            return

        self.persona_servicio.eliminar_persona(self.id_seleccionado)
        self.cargar_datos()
        self.limpiar_campos()

    def limpiar_campos(self):
        self.entry_dni.delete(0, tk.END)
        self.entry_nombres.delete(0, tk.END)
        self.entry_apellidos.delete(0, tk.END)
        self.combo_sexo.current(0)
        self.id_seleccionado = None
    
    def validar_dni(self,valor):
        if valor.isdigit() and len(valor) <=8:
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