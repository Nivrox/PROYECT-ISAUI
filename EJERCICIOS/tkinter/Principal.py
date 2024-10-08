import tkinter as tk
from tkinter import messagebox
from Viewalta import abrir_ventana_alta  # Importamos las funciones
from Viewlistado import abrir_ventana_listado

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menú Principal - Sistema de Preinscripción ISAUI")
        self.geometry("450x300+450+300")
        self.config(bg="#b39658")

        btn_alta = tk.Button(self, text="Formulario de Alta", command=self.abrir_alta, font=('Calibri', 15), bg="#ffffff", width=25)
        btn_alta.pack(pady=20)

        btn_listado = tk.Button(self, text="Listado de Personas", command=self.abrir_listado, font=('Calibri', 15), bg="#ffffff", width=25)
        btn_listado.pack(pady=20)

        btn_salir = tk.Button(self, text="Salir", command=self.salir, font=('Calibri', 15), bg="#ffffff", width=25)
        btn_salir.pack(pady=20)

    def abrir_alta(self):
        abrir_ventana_alta()

    def abrir_listado(self):
        abrir_ventana_listado()


    def salir(self):
        if messagebox.askyesno("Confirmar", "¿Desea salir del sistema?"):
            self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()