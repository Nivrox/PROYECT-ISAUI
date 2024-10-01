import tkinter as tk
from tkinter import messagebox
import mysql.connector 

# Datos de conexión a la base de datos (reemplázalos con tus datos)
mydb = mysql.connector.connect(
        host="localhost",
        user="root", #PONER SU PROPIO USUARIO
        password="bru455no", #PONER SU PROPIA CLAVE
        database="isaui")
mycursor = mydb.cursor()

def insertar_persona(apellido,nombre,dni,telefono,correo,domicilio,ciudad,instagram,carrera):
        try:
            
            sql = "INSERT INTO personas (apellido, nombre, dni, telefono, correo, domicilio, ciudad,instagram,id_carreras) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (apellido, nombre, dni, telefono, correo, domicilio, ciudad, instagram,carrera)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Éxito", "Registro insertado correctamente.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al insertar en la base de datos: {err}")