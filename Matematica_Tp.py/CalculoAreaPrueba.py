import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import tkinter as tk
from tkinter import messagebox

def evaluar_funcion(expr, x):
    try:
        return eval(expr)
    except Exception as e:
        messagebox.showerror("Error", f"Error al evaluar la función: {e}")
        return None

def calcular_area():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        n = int(entry_n.get())
        funcion = entry_funcion.get()

        if n <= 0:
            messagebox.showerror("Error", "El número de rectángulos debe ser positivo.")
            return

        delta_x = (b - a) / n
        sum_inferior = 0
        sum_superior = 0

        x_plot = np.linspace(a, b, 100)
        y_plot = [evaluar_funcion(funcion, x) for x in x_plot]

        plt.figure(figsize=(10, 6))
        plt.plot(x_plot, y_plot, label=f"f(x) = {funcion}", color='blue')

        # Suma Inferior
        for i in range(n - 1):
            x_izquierdo = a + i * delta_x
            altura_izquierda = evaluar_funcion(funcion, x_izquierdo)

            # Dibuja el rectángulo de la suma inferior
            plt.bar(x_izquierdo, altura_izquierda, width=delta_x, alpha=0.3, align='edge', color='green', edgecolor='black')
            sum_inferior += altura_izquierda * delta_x

        # Suma Superior
        for i in range(n - 1):
            x_derecho = a + (i + 1) * delta_x
            altura_derecha = evaluar_funcion(funcion, x_derecho)

            # Dibuja el rectángulo de la suma superior
            plt.bar(x_derecho - delta_x, altura_derecha, width=delta_x, alpha=0.3, align='edge', color='red', edgecolor='black')
            sum_superior += altura_derecha * delta_x

        # Calcular el área real usando integración numérica
        area_real, _ = quad(lambda x: evaluar_funcion(funcion, x), a, b)

        # Mostrar resultados
        plt.text(a + (b - a) / 2, max(y_plot) * 0.8,
                 f"Suma Inferior: {sum_inferior:.4f}\nSuma Superior: {sum_superior:.4f}\nÁrea Real: {area_real:.4f}",
                 fontsize=12, ha='center', bbox=dict(facecolor='white', alpha=0.7))

        plt.title('Área bajo la curva')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.xlim(a - 1, b + 1)  # Ajustar límites del gráfico
        plt.ylim(min(y_plot) - 2, max(y_plot) + 2)
        plt.legend()
        plt.grid(True)
        plt.show()

        # Limpiar entradas
        entry_a.delete(0, tk.END)
        entry_b.delete(0, tk.END)
        entry_n.delete(0, tk.END)
        entry_funcion.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos.")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Calcula el Área")
root.configure(bg="#8f7456")
root.geometry("300x350")

# Crear un marco para las entradas
frame = tk.Frame(root, bd=2, relief=tk.RIDGE, bg="#bdb19d", height=300, width=200)
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
