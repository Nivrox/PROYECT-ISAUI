import tkinter as tk
import tkinter as ttk
from tkinter import *
from tkinter import messagebox

class FormularioClientes:

    def formulario():

        try:    
            base = tk.Tk()
            base.geometry("1250x300")
            base.title("Formulario de clientes")
            

            groupBox = LabelFrame(base, text = "Datos Personales", pady=5,padx=5)
            groupBox.grid(row=0, column=0, padx=10, pady=10)
            
            labeldni= Label(groupBox, text="Dni:", width=13, font=("Arial", 12))
            labeldni.grid(row=0, column=0, sticky="w")

            base.mainloop()
        except ValueError as e: 
            print("Error al crear el formulario: {}".format(e))

    formulario()