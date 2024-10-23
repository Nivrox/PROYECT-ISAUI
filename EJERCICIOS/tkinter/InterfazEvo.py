import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import ttkbootstrap as ttk
from tkinter import messagebox

# Definir la función cuadrática
def f_cuadratica(x):
    return x**2

def calcular_area():
    try:
        # Obtener los valores ingresados
        a = float(entry_a.get())
        b = float(entry_b.get())
        n = int(entry_n.get())

        if n <= 0:
            messagebox.showerror("Error", "El número de rectángulos debe ser positivo.")
            return

        # Calcular el ancho de cada rectángulo
        delta_x = (b - a) / n

        # Inicializar las sumas
        sum_inferior = 0
        sum_superior = 0

        # Crear la gráfica
        x_plot = np.linspace(a, b, 100)
        y_plot = f_cuadratica(x_plot)

        plt.figure(figsize=(10, 6))
        plt.plot(x_plot, y_plot, label="f(x) = x^2", color='blue')

        # Dibujar los rectángulos y colorear según las condiciones
        for i in range(n):
            x_izquierdo = a + i * delta_x
            x_derecho = a + (i + 1) * delta_x
            altura_derecha = f_cuadratica(x_derecho)
            altura_izquierda = f_cuadratica(x_izquierdo)

            # Parte inferior (debajo de la curva)
            if altura_derecha <= altura_izquierda:
                plt.bar(x_derecho, altura_derecha, width=-delta_x, alpha=0.3, align='edge', color='red', edgecolor='black')
            else:
                # Parte superior (sobre la curva)
                plt.bar(x_derecho, altura_izquierda, width=-delta_x, alpha=0.3, align='edge', color='red', edgecolor='black')
                # Solo la parte que sobrepasa la curva
                plt.bar(x_derecho, altura_derecha - altura_izquierda, bottom=altura_izquierda, width=-delta_x, alpha=0.6, align='edge', color='green', edgecolor='black')

            # Sumar el área de los rectángulos
            sum_inferior += altura_izquierda * delta_x
            sum_superior += altura_derecha * delta_x

        # Calcular el área real usando integración numérica
        area_real, _ = quad(f_cuadratica, a, b)

        # Mostrar los resultados en la gráfica
        plt.text(a + (b - a) / 2, max(y_plot) * 0.8,
                 f"Suma Inferior: {sum_inferior:.4f}\nSuma Superior: {sum_superior:.4f}\nÁrea Real: {area_real:.4f}",
                 fontsize=12, ha='center', bbox=dict(facecolor='white', alpha=0.7))

        plt.title('Área bajo la curva f(x) = x^2')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.xlim(a, b)
        plt.ylim(0, max(y_plot) * 1.1)
        plt.legend()
        plt.grid(True)
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos.")

# Crear la interfaz gráfica con ttkbootstrap
root = ttk.Window(themename="flatly")
root.title("Calcula la Función Cuadrática")
root.geometry("300x300")

# Crear un marco para las entradas
frame = ttk.Frame(root, padding=10)
frame.pack(padx=10, pady=10)
frame.configure(style='TFrame')
style = ttk.Style()
style.configure('TFrame', background='#bdb19d')  # Cambia el color aquí
# Etiquetas y campos de entrada
label_titulo = ttk.Label(frame, text="Calcula el Área", font=("Arial", 14), background='#bdb19d')
label_titulo.pack(pady=5)

style = ttk.Style()
style.configure('TEntry', font=('Arial', 12), padding=5, borderwidth=4, relief="solid")

# Los campos de entrada redondeados
entry_a = ttk.Entry(frame, style='TEntry', bootstyle="success")
entry_a.pack(pady=5)

label_a = ttk.Label(frame, text="Límite Inferior (a):",  background='#bdb19d' )
label_a.pack()

entry_b = ttk.Entry(frame, style='TEntry', bootstyle="success",)
entry_b.pack(pady=5)

label_b = ttk.Label(frame, text="Límite Superior (b):",background='#bdb19d')
label_b.pack()

entry_n = ttk.Entry(frame, style='TEntry', bootstyle="success")
entry_n.pack(pady=5)

label_n = ttk.Label(frame, text="Número de Rectángulos (n):",background='#bdb19d')
label_n.pack()

# Botón para calcular el área
button_calcular = ttk.Button(root, text="Calcular Área", command=calcular_area)
button_calcular.pack(pady=10)

# Iniciar el bucle de la interfaz
root.mainloop()
