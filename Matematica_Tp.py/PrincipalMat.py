import tkinter as tk
from tkinter import messagebox
from MetodoGauss import ventana_gauss 
from CalculoArea import ventana_area


def ventana_principal():
    try:
        ventana = tk.Tk()
        ventana.title("Menú Principal - Sistema de Preinscripción ISAUI")
        ventana.geometry("450x300+450+300")
        ventana.config(bg="#b39658")

        def abrir_gauss():
            ventana_gauss()

        def abrir_area():
            ventana_area()


        def salir(ventana):
            if messagebox.askyesno("Confirmar", "¿Desea salir del sistema?"):
                ventana.destroy()
        
        btn_gauss = tk.Button(ventana, text="Ecuaciones de lineales", command=abrir_gauss, font=('Calibri', 15), bg="#ffffff", width=25)
        btn_gauss.pack(pady=20)

        btn_area = tk.Button(ventana, text="Area bajo la curva", command= abrir_area, font=('Calibri', 15), bg="#ffffff", width=25)
        btn_area.pack(pady=20)

        btn_salir = tk.Button(ventana, text="Salir", command=salir, font=('Calibri', 15), bg="#ffffff", width=25)
        btn_salir.pack(pady=20)
        ventana.mainloop()
        
    except ValueError as error:
            print("Error al mostrar la interfaz, error{}".format(error))

    
ventana_principal()