import tkinter as tk
from AreaBajoLaCurva import *   
def ventana_principal():
    try:
        ventana = tk.Tk()
        ventana.title("Menú Principal - Sistema de Preinscripción ISAUI")
        ventana.geometry("450x300+450+300")
        ventana.config(bg="#b39658")

        def abrir_alta():
            ventana_gauss()

        def abrir_listado():
            Area_bajo_Curva()

        def salir(ventana):
            if messagebox.askyesno("Confirmar", "¿Desea salir del sistema?"):
                    ventana.destroy()

    
    except ValueError as error:
            print("Error al mostrar la interfaz, error{}".format(error))
    btn_alta = tk.Button(ventana, text="Cacular ecuaciones lineales", command=abrir_alta, font=('Calibri', 15), bg="#ffffff", width=25)
    btn_alta.pack(pady=20)

    btn_listado = tk.Button(ventana, text="Calcular area bajo la curva", command=abrir_listado, font=('Calibri', 15), bg="#ffffff", width=25)
    btn_listado.pack(pady=20)
    btn_salir = tk.Button(ventana, text="Salir", command=salir, font=('Calibri', 15), bg="#ffffff", width=25)
    btn_salir.pack(pady=20)
    ventana.mainloop()
ventana_principal()