import tkinter as tk
#importar los modulos restantes de tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Clientes import *
from conexion import *
class FormularioClientes:
    
    global texboxdni
    texboxdni = None
    
    global texboxNombre
    texboxNombre = None
    
    global texboxApellido
    texboxApellido = None
    
    global seleccionSexo
    seleccionSexo = None
    
    global tree
    tree = None
    
    global groupBox
    groupBox = None

    global base
    base = None

def Formulario():
    global texboxdni
    global texboxNombre
    global texboxApellido
    global seleccionSexo
    global tree
    global groupBox
    global base

    try:
        base = Tk()        
        base.geometry("1250x300")
        base.title("Formulario de Clientes")
                

        groupBox = LabelFrame(base, text="Datos de Personal", padx=5, pady=5)
        groupBox.grid(row=0, column=0, padx=10, pady=10)

        LabelId = Label(groupBox, text="Dni:", width= 13, font=("Arial", 12)).grid(row=0, column=0)
        texboxdni = Entry(groupBox, width=20, font=("Arial", 12))
        texboxdni.grid(row=0, column=1)

        labelNombre = Label(groupBox, text="Nombres:", width= 13, font=("Arial", 12)).grid(row=1, column=0)
        texboxNombre = Entry(groupBox, width=20, font=("Arial", 12))
        texboxNombre.grid(row=1, column=1)

        labelApellido = Label(groupBox, text="Apellido:", width= 13, font= ("Arial", 12)).grid(row = 2, column = 0)
        texboxApellido = Entry (groupBox, width=20, font=("Arial", 12))
        texboxApellido.grid (row=2, column=1)

        labelSexo = Label(groupBox, text="Sexo", width= 12, font=("Arial", 12)).grid(row=3, column=0)
        seleccionSexo = tk.StringVar()
        comboSexo = ttk.Combobox(groupBox, values= ["Masculino", "Femenino", "Otro"], textvariable= seleccionSexo)
        comboSexo.grid(row=3, column=1)
        seleccionSexo.set("Masculino")

        botonGuardar = Button(groupBox, text="Guardar", width=10, command=guardarRegistros ).grid(row=4, column=0, pady=10)

        botonModificar = Button(groupBox, text="Modificar", width=10, command=modificarRegistros).grid(row = 4, column=1, pady=10)

        botonEliminar = Button(groupBox, text="Eliminar", width=10, command=eliminarRegistros).grid(row = 4, column=2, pady=10)

        groupBox = LabelFrame (base, text="Lista de Datos", padx=5, pady=5)
        groupBox.grid(row=0, column=1, padx=5, pady=5)

        tree = ttk.Treeview(groupBox, columns=("Nombres", "Apellidos", "Sexo", "Dni"), show='headings', height=5)
        tree.column("#1", anchor=CENTER)
        tree.heading("#1", text="Nombres")
        tree.column("#2", anchor=CENTER)
        tree.heading("#2", text="Apellidos")
        tree.column("#3", anchor=CENTER)
        tree.heading("#3", text="Sexo")
        tree.column("#4", anchor=CENTER)
        tree.heading("#4", text="Dni")

        #agregar los datos a la tabla
        for row in Ppersonas.mostrarPersonas():
            tree.insert("","end",values=row)

        #Ejecutar la funcion de seleccion de registro y mostrar los datos en los campos de texto
        tree.bind("<<TreeviewSelect>>", seleccionarRegistro)

        tree.pack()

        base.mainloop()
    except ValueError as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al mostrar la interfaz : {e}")

def guardarRegistros():
    global texboxdni, texboxNombre, texboxApellido, seleccionSexo, groupBox
    try:
            #Verificar si estan inicializados los campos
        if texboxdni is None or texboxNombre is None or texboxApellido is None or seleccionSexo is None:
            print ("Llena Todos los Campos")
            return
        
        nombres = texboxNombre.get()
        apellidos = texboxApellido.get()
        sexo = seleccionSexo.get()
        dni = texboxdni.get()
        Ppersonas.ingresarPersonas(nombres, apellidos, sexo, dni)
        messagebox.showinfo("Exito", "Datos guardados correctamente")

        #limpiamos los campos de texto 
        actualizarTreeview()
        texboxNombre.delete(0, END)
        texboxApellido.delete(0, END)
        texboxdni.delete(0, END)

    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al guardar los registros: {e}")

def actualizarTreeview():
    global tree 
    try:
        #borrar todos los elementos actuales del treeview
        tree.delete(*tree.get_children())
        #obtener los nuevos datos que deseamos mostrar 
        datos = Ppersonas.mostrarPersonas()
        for row in datos:
            tree.insert("","end",values=row)
    except ValueError as e:
        print("Error, Ha ocurrido un error al actualizar la lista:{}".format(e))

def seleccionarRegistro(event):
    try:
        seleccion = tree.focus()

        if seleccion:
            #obtener los valores de las columnas del item seleccionado
            values = tree.item(seleccion) ['values']

            #Establecer los valores en los widgets de entrada
            texboxNombre.delete(0, END)
            texboxNombre.insert(0, values[0])
            texboxApellido.delete(0, END)
            texboxApellido.insert(0, values[1])
            texboxdni.delete(0, END)
            texboxdni.insert(0, values[3])
            seleccionSexo.set(values[2])

    except ValueError as error:
        print ("Error al seleccionar el registro: {}".format(error))

def modificarRegistros():
    global texboxNombre, texboxApellido, seleccionSexo, texboxdni, groupBox
    
    try:
            #Verificar si estan inicializados los campos
        if texboxdni is None or texboxNombre is None or texboxApellido is None or seleccionSexo is None:
            print ("Llena Todos los Campos")
            return
        
        nombres = texboxNombre.get()
        apellidos = texboxApellido.get()
        sexo = seleccionSexo.get()
        dni = texboxdni.get()
        Ppersonas.modificarPersonas(nombres,apellidos,sexo,dni)
        messagebox.showinfo("Exito", "Datos Modificados correctamente")

        #limpiamos los campos de texto 
        actualizarTreeview()
        texboxNombre.delete(0, END)
        texboxApellido.delete(0, END)
        texboxdni.delete(0, END)

    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al modificar los registros: {e}")

def eliminarRegistros():
    global texboxNombre, texboxApellido, seleccionSexo, texboxdni, groupBox

    try:
        #Verificar si estan inicializados los campos
        if texboxdni is None or texboxNombre is None or texboxApellido is None or seleccionSexo is None:
            print ("Llena Todos los Campos")
            return
        
        nombres = texboxNombre.get()
        apellidos = texboxApellido.get()
        sexo = seleccionSexo.get()
        dni = texboxdni.get()
        Ppersonas.eliminarPersonas(nombres,apellidos,sexo,dni)
        messagebox.showinfo("Exito", "Datos Eliminados correctamente")

        #limpiamos los campos de texto 
        actualizarTreeview()
        texboxNombre.delete(0, END)
        texboxApellido.delete(0, END)
        texboxdni.delete(0, END)

    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al modificar los registros: {e}")
Formulario()