import re
from tkinter import messagebox


def verificar_correo(correo):

    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
   
    if not re.match(patron, correo):
        messagebox.showerror("Error", f"{correo} : no es una dirección de correo válida.")
        return False
    return True
    
def validar_dni(dni):
    
    if not dni.isdigit():  
        messagebox.showerror("Error", "Solamente se aceptan dígitos en el dni")
        return False
    elif len(dni) < 7 or len(dni) > 8:  
        messagebox.showerror("Error", "El DNI debe tener 7 u 8 dígitos")
        return   False   
    return True

def validar_telefono(telefono):
    if not telefono.isdigit():  
        messagebox.showerror("Error", "Solamente se aceptan dígitos")
        return False
    elif len(telefono) < 6 or len(telefono) > 10:
        messagebox.showerror("Error", "El número de teléfono debe tener entre 6 y 10 dígitos")
        return False
    return True

def validar_campos_obligatorios(entries):
    if all(entry.get().strip() == "" for entry in entries):
        messagebox.showerror("Error", "Todos los campos del formulario son obligatorios.")
        return False
    return True

