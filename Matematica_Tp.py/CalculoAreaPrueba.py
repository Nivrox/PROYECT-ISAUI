import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import tkinter as tk
from tkinter import messagebox
import re

# Función para evaluar la expresión ingresada
def evaluar_funcion(expr, x):
    try:
        return eval(expr)
    except Exception as e:
        raise ValueError(f"Error al evaluar la función: {e}")

# Función para validar si la entrada es una función cuadrática válida
def es_funcion_cuadratica(funcion):
    # Eliminar espacios en blanco
    funcion = funcion.replace(' ', '')
    
    # Expresión regular que captura cualquier combinación válida de ax^2, bx y c
    patron = r'^(-?\d*\.?\d*)?x\*\*2([-+]\d*\.?\d*x?)?([-+]\d*\.?\d*)?$'
    
    # Validar si coincide con el patrón de una función cuadrática
    if re.match(patron, funcion):
        return True
    return False

# Función para dibujar los rectángulos
def dibujar_rectangulos(a, b, n, funcion, sum_inferior, sum_superior, area_real):
    delta_x = (b - a) / n
    x_plot = np.linspace(a, b, 100)
    y_plot = [evaluar_funcion(funcion, x) for x in x_plot]

    plt.figure(figsize=(10, 6))
    plt.plot(x_plot, y_plot, label=f"f(x) = {funcion}", color='blue')

    # Dibujar los rectángulos de la suma inferior (borde izquierdo)
    for i in range(n):
        x_izquierdo = a + i * delta_x
        altura_izquierda = evaluar_funcion(funcion, x_izquierdo)
        if altura_izquierda is not None:
            plt.bar(x_izquierdo, altura_izquierda, width=delta_x, alpha=0.3, align='edge', color='green', edgecolor='black')

    # Dibujar los rectángulos de la suma superior (borde derecho)
    for i in range(n):
        x_derecho = a + (i + 1) * delta_x
        altura_derecha = evaluar_funcion(funcion, x_derecho)
        if altura_derecha is not None:
            plt.bar(x_derecho - delta_x, altura_derecha, width=delta_x, alpha=0.3, align='edge', color='green', edgecolor='black')

    # Mostrar los resultados en el gráfico
    plt.text(a + (b - a) / 2, max(y_plot) * 0.8,
             f"Suma Inferior: {sum_inferior:.4f}\nSuma Superior: {sum_superior:.4f}\nÁrea Real: {area_real:.4f}",
             fontsize=12, ha='center', bbox=dict(facecolor='white', alpha=0.7))

    plt.title('Rectángulos de la Suma Inferior y Superior')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.xlim(a - 4, b + 4)
    plt.ylim(0, max(y_plot) + 3)
    plt.grid(True)
    plt.legend()
    plt.show()

# Función para calcular la suma inferior y superior
def calcular_sumas_inferior_superior(a, b, n, funcion):
    delta_x = (b - a) / n
    sum_inferior = 0
    sum_superior = 0

    for i in range(n - 1):
        # Borde izquierdo para suma inferior
        x_izquierdo = a + i * delta_x
        altura_izquierda = evaluar_funcion(funcion, x_izquierdo)
        if altura_izquierda is not None:
            sum_superior += altura_izquierda * delta_x

        # Borde derecho para suma superior
        x_derecho = a + (i + 1) * delta_x
        altura_derecha = evaluar_funcion(funcion, x_derecho)
        if altura_derecha is not None:
            sum_inferior += altura_derecha * delta_x

    return sum_inferior, sum_superior

# Función que se ejecuta al presionar el botón de calcular
def calcular_area():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        n = int(entry_n.get())
        funcion = entry_funcion.get()

        if n <= 0:
            messagebox.showerror("Error", "El número de rectángulos debe ser positivo.")
            return

        if not es_funcion_cuadratica(funcion):
            messagebox.showerror("Error", "Por favor ingrese una función cuadrática válida (ej: 2*x**2 + 3*x + 1).")
            return

        # Calcular las áreas de los rectángulos
        sum_inferior, sum_superior = calcular_sumas_inferior_superior(a, b, n, funcion)

        # Calcular el área real usando integración numérica
        area_real, _ = quad(lambda x: evaluar_funcion(funcion, x), a, b)

        # Llamar a la función para dibujar los rectángulos y mostrar los resultados
        dibujar_rectangulos(a, b, n, funcion, sum_inferior, sum_superior, area_real)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Calcula el Área")
root.configure(bg="#8f7456")
root.geometry("300x400")

# Crear un marco para las entradas
frame = tk.Frame(root, bd=2, relief=tk.RIDGE, bg="#bdb19d")
frame.pack(padx=10, pady=10, fill='y', expand=True)

# Etiquetas y campos de entrada
label_titulo = tk.Label(frame, text="Calcula el Área", font=("Arial", 14), bg="#bdb19d")
label_titulo.pack(pady=5)

label_funcion = tk.Label(frame, text="Introduce la función cuadrática (ej: 2*x**2 + 3*x + 1):", bg="#bdb19d")
label_funcion.pack()
entry_funcion = tk.Entry(frame)
entry_funcion.pack()

label_inferior = tk.Label(frame, text="Límite Inferior (a):", bg="#bdb19d")
label_inferior.pack()
entry_a = tk.Entry(frame)
entry_a.pack()

label_superior = tk.Label(frame, text="Límite Superior (b):", bg="#bdb19d")
label_superior.pack()
entry_b = tk.Entry(frame)
entry_b.pack()

label_rectangulos = tk.Label(frame, text="Número de Rectángulos (n):", bg="#bdb19d")
label_rectangulos.pack()
entry_n = tk.Entry(frame)
entry_n.pack()

# Botón para calcular el área
button_calcular = tk.Button(root, text="Calcular Área", command=calcular_area)
button_calcular.pack(pady=10)

# Iniciar el bucle de la interfaz
root.mainloop()
