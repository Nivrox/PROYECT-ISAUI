import tkinter as tk
from tkcalendar import DateEntry
from datetime import datetime

ventana_prestamos = tk.Tk()

# Crear el DateEntry y configurarlo correctamente
tk.Label(ventana_prestamos, text="Fecha Préstamo", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
devolucion_entry1 = DateEntry(ventana_prestamos, font=("Arial", 12), width=23, background="lightgreen", foreground="black", borderwidth=2, locale="es_Es", date_pattern='dd/MM/yyyy')
devolucion_entry1.pack(pady=5)

def obtener_fecha():
    # Obtener la fecha como cadena desde el DateEntry
    fecha_devolucion_str = devolucion_entry1.get()
    # Convertir la cadena en un objeto de fecha
    fecha_devolucion = datetime.strptime(fecha_devolucion_str, "%d/%m/%Y").date()
    print("Fecha de devolución:", fecha_devolucion)

# Botón para probar la obtención de la fecha
boton = tk.Button(ventana_prestamos, text="Obtener Fecha", command=obtener_fecha)
boton.pack()

ventana_prestamos.mainloop()