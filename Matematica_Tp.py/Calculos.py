import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import tkinter as tk
from tkinter import messagebox
import sympy as sp

# Función para evaluar la expresión cuadrática
def funcion_cuadratica(x, a, b, c):
    return a * x**2 + b * x + c

# Función para dibujar los rectángulos
def dibujar_rectangulos(a, b, n, funcion, sum_inferior, sum_superior, area_real):
    delta_x = (b - a) / n
    x_plot = np.linspace(a, b, 100)
    y_plot = [funcion(x) for x in x_plot]  # Se evalúa la función numéricamente

    plt.figure(figsize=(10, 6))
    plt.plot(x_plot, y_plot, label=f"f(x)", color='blue')

    # Dibujar los rectángulos de la suma inferior (borde izquierdo)
    for i in range(n):
        x_izquierdo = a + i * delta_x
        altura_izquierda = funcion(x_izquierdo)
        plt.bar(x_izquierdo, altura_izquierda, width=delta_x, alpha=0.3, align='edge', color='green', edgecolor='black')

    # Dibujar los rectángulos de la suma superior (borde derecho)
    for i in range(n):
        x_derecho = a + (i + 1) * delta_x
        altura_derecha = funcion(x_derecho)
        plt.bar(x_derecho - delta_x, altura_derecha, width=delta_x, alpha=0.3, align='edge', color='green', edgecolor='black')

    # Mostrar los resultados en el gráfico
    plt.text(a + (b - a) / 2, max(y_plot) * 0.8,
             f"Suma Inferior: {sum_inferior:.4f}\nSuma Superior: {sum_superior:.4f}\nÁrea Real: {area_real:.4f}",
             fontsize=12, ha='center', bbox=dict(facecolor='white', alpha=0.7))

    plt.title('Rectángulos de la Suma Inferior y Superior')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.xlim(a, b)
    plt.ylim(0, max(y_plot) + 3)
    plt.grid(True)
    plt.legend()
    plt.show()

# Función para calcular la suma inferior y superior
def calcular_sumas_inferior_superior(a, b, n, funcion):
    delta_x = (b - a) / n  # Ancho de cada rectángulo
    suma_inferior = 0
    suma_superior = 0

    # Dividimos el intervalo en puntos
    x_values = np.linspace(a, b, n + 1)  # n+1 puntos para n rectángulos

    # Evaluamos la función en esos puntos
    y_values = [funcion(x) for x in x_values]

    # Calculamos la suma inferior y superior
    for i in range(n):
        # Alturas en los extremos del intervalo
        altura_izquierda = y_values[i]
        altura_derecha = y_values[i + 1]

        # Suma inferior: usamos la menor de las dos alturas
        suma_inferior += delta_x * min(altura_izquierda, altura_derecha)

        # Suma superior: usamos la mayor de las dos alturas
        suma_superior += delta_x * max(altura_izquierda, altura_derecha)

    return suma_inferior, suma_superior

# Función que se ejecuta al presionar el botón de calcular
def calcular_area():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        n = int(entry_n.get())
        funcion_str = entry_funcion.get()

        if n <= 0:
            messagebox.showerror("Error", "El número de rectángulos debe ser positivo.")
            return

        # Convertir la expresión de la función a una función numérica
        x = sp.symbols('x')
        expresion = sp.sympify(funcion_str)
        funcion_numerica = sp.lambdify(x, expresion)  # Convierte la función simbólica a numérica

        # Calcular las áreas de los rectángulos
        sum_inferior, sum_superior = calcular_sumas_inferior_superior(a, b, n, funcion_numerica)

        # Calcular el área real usando integración numérica
        area_real, _ = quad(funcion_numerica, a, b)

        # Llamar a la función para dibujar los rectángulos y mostrar los resultados
        dibujar_rectangulos(a, b, n, funcion_numerica, sum_inferior, sum_superior, area_real)

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

label_funcion = tk.Label(frame, text="Introduce la función (ej: x**2):", bg="#bdb19d")
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
