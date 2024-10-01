import re
from tkinter import messagebox

#Validar correo electronico
def verificar_correo(correo):
    # Expresión regular para validar el formato del correo electrónico
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # Comprobar si el correo cumple con el patrón
    if not re.match(patron, correo):
        messagebox.showerror("Error", f"{correo} : no es una dirección de correo válida.")
        return False
    return True
    
def validar_dni(dni):
    
    if not dni.isdigit():  # Verifica si el DNI tiene solo números
        messagebox.showerror("Error", "Solamente se aceptan dígitos")
        return False
    elif len(dni) < 7 or len(dni) > 8:  # Verifica que el DNI tenga 7 u 8 dígitos
        messagebox.showerror("Error", "El número debe tener 7 u 8 dígitos")
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