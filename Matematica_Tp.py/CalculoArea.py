import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter as messagebox
def ventana_area():
    
    
    def calcular_area_cuadratica(a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos):
        def funcion_cuadratica(x):
            return a * x**2 + b * x + c
        
        area_real, _ = quad(lambda x : abs (funcion_cuadratica (x)), intervalo_inicio, intervalo_fin)

        x_values = np.linspace(intervalo_inicio, intervalo_fin, num_rectangulos + 1)
        y_values = [abs(funcion_cuadratica(x)) for x in x_values]

        suma_inferior = 0 
        suma_superior = 0 

        for i in range (num_rectangulos):
            ancho = x_values[i +1] - x_values[i]
            suma_inferior += ancho * min(y_values[i], y_values[i + 1])
            suma_superior += ancho * max(y_values[i], y_values[i + 1])
        
        error = area_real - (suma_inferior + suma_superior) / 2

        return suma_inferior, suma_superior, abs, (error)

    def graficar_funcion (a,b,c, intervalo_inicio, intervalo_fin, num_rectangulos, texto_resultado):
        x_plot = np.linspace (intervalo_inicio,intervalo_fin)
        y_plot = [a * x**2 + b * x + c for x in x_plot]

        plt.plot(x_plot,y_plot, label= 'Funcion cuadratica', color = 'blue')
        plt.fill_between(x_plot, y_plot, color='blue', alpha=0.1)

        ancho = (intervalo_fin - intervalo_inicio) / num_rectangulos
        for i in range (num_rectangulos):
            xi = intervalo_inicio + i * ancho
            xf = intervalo_inicio + (i + 1) * ancho
            altura_inferior = min(a * xi **2 + b * xi + c, a * xf**2 + b* xf+ c)
            altura_superior = max(a * xi**2 + b *xi + c, a * xf **2 + b * xf + c)
            plt.bar (xi, altura_inferior, width = ancho, color = 'yellow', alpha = 0.5, edgecolor = 'black', align = 'edge' )
            plt.bar(xi, altura_superior, width = ancho, color = 'pink', alpha = 0.3, edgecolor = 'black', align = 'edge')

            plt.text(0.5, 0.5, texto_resultado, fontsize = 12, ha = 'center', transform= plt.gca().transAxes)
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title('Grafico de la funcion cuadratica con sumas inferior y superior')
            plt.legend()
            plt.grid(True)
            plt.show()
    def calcular_area():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())
            intervalo_inicio = float(entry_intervalo_inicio.get())
            intervalo_fin = float(entry_intervalo_fin.get())
            num_rectangulos = int(entry_num_rectangulos.get())

            if num_rectangulos <= 0:
                messagebox.showerror("Error", "El número de rectángulos debe ser positivo.")
                return

            suma_inferior, suma_superior, area_real, error = calcular_area_cuadratica(
                a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos
            )

            texto_resultado = (f"Suma Inferior: {suma_inferior:.4f}\nSuma Superior: {suma_superior:.4f}\nÁrea Real: {area_real:.4f}\nError: {error:.4f}")
            graficar_funcion(a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos, texto_resultado)

        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    ventanaArea = tk.Tk()
    ventanaArea.title("Cálculo de Área")
    ventanaArea.geometry("400x400")
    ventanaArea.configure(bg="#dde")

    # Campos de entrada para los parámetros de la función cuadrática y el cálculo
    tk.Label(ventanaArea, text="Coeficiente a:").pack()
    entry_a = tk.Entry(ventanaArea)
    entry_a.pack()

    tk.Label(ventanaArea, text="Coeficiente b:").pack()
    entry_b = tk.Entry(ventanaArea)
    entry_b.pack()

    tk.Label(ventanaArea, text="Coeficiente c:").pack()
    entry_c = tk.Entry(ventanaArea)
    entry_c.pack()

    tk.Label(ventanaArea, text="Intervalo Inicio:").pack()
    entry_intervalo_inicio = tk.Entry(ventanaArea)
    entry_intervalo_inicio.pack()

    tk.Label(ventanaArea, text="Intervalo Fin:").pack()
    entry_intervalo_fin = tk.Entry(ventanaArea)
    entry_intervalo_fin.pack()

    tk.Label(ventanaArea, text="Número de Rectángulos:").pack()
    entry_num_rectangulos = tk.Entry(ventanaArea)
    entry_num_rectangulos.pack()

    # Botón para calcular el área
    button_calcular = tk.Button(ventanaArea, text="Calcular Área", command=calcular_area)
    button_calcular.pack(pady=10)

    # Iniciar la interfaz gráfica
    ventanaArea.mainloop()
if __name__ == "__main__":
    ventana_area()