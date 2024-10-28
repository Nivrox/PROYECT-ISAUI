import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from datetime import datetime
from tkinter import messagebox


        
        
            
        
def validar_fechas(fecha_prestamo, fecha_devolucion):

            try:
                
                fecha_prestamo_dt = datetime.strptime(fecha_prestamo, "%d/%m/%Y")
                fecha_devolucion_dt = datetime.strptime(fecha_devolucion, "%d/%m/%Y")
            except ValueError:
                messagebox.showwarning("Formato inválido", "El formato de la fecha debe ser DD/MM/YYYY.")
                return False

        
            fecha_hoy = datetime.today()

        
            if fecha_prestamo_dt < fecha_hoy:
                messagebox.showwarning("Fecha inválida", "La fecha de préstamo no puede ser anterior a la fecha de hoy.")
                return False  # Fecha inválida

        
            if fecha_devolucion_dt < fecha_prestamo_dt:
                messagebox.showwarning("Fecha inválida", "La fecha de devolución no puede ser anterior a la fecha de préstamo.")
                return False  # Fecha inválida

            return True  # Ambas fechas son válidas


        
def validar_palabras(texto):
            # Divide el texto en palabras utilizando espacios como delimitador
            palabras = texto.split()
            
            # Verifica que el número de palabras sea igual a 8
            if len(palabras) != 8:
                messagebox.showwarning("Número de palabras inválido", "Debes ingresar exactamente 8 palabras.")
                return False  # Número de palabras no válido
            return True  # Número de palabras válido

def validar_palabras(entry_value):
            # Divide el texto en palabras utilizando espacios como delimitador
            palabras = entry_value.split()
            
            # Permite la entrada si el número de palabras es 20 o menos
            return len(palabras) <= 20

def validar_dni(dni):
            
            if not dni.isdigit():  # Verifica si el DNI tiene solo números
                messagebox.showerror("Error", "Solamente se aceptan dígitos en la busqueda")
                return False
            elif len(dni) < 7 or len(dni) > 8:  # Verifica que el DNI tenga 7 u 8 dígitos
                messagebox.showerror("Error", "El DNI debe tener 7 u 8 dígitos")
                return   False   
            return True

def validar_isbn(isbn):
            
            if not isbn.isdigit():  # Verifica si el DNI tiene solo números
                messagebox.showerror("Error", "Solamente se aceptan dígitos en la busqueda")
                return False
            elif len(isbn) < 4 or len(isbn) > 5:  # Verifica que el DNI tenga 7 u 8 dígitos
                messagebox.showerror("Error", "El ISBN debe tener 5 dígitos")
                return   False   
            return True

def validar_entrada(parametro):
    
    try:
        patron = r'^\w{0,10}$'
        if parametro == patron:
            return True
    
    except:
            messagebox.showwarning("Advertencia", "Solo se permiten numeros")
            return None
def manejar_invalidacion():
            
            return None