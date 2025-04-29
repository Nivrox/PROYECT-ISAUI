import numpy as np
from scipy.integrate import quad 

def calcular_area_cuadratica(a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos):
    def funcion_cuadratica(x):
        return a * x**2 + b * x + c
    
    area_real, _ = quad(lambda x : abs (funcion_cuadratica (x)), intervalo_inicio, intervalo_fin))

    x_values = np.linspace(intervalo_inicio, intervalo_fin, num_rectangulos + 1)
    y_values = [abs(funcion_cuadratica(x)) for x in x_values]

    suma_inferior = 0 
    suma_superior = 0 

    for i in range (num_rectangulos):
        ancho = x_values[i +1] - x_values[i]
        suma_inferior += ancho * min(y_values[i], y_values[i + 1])
        suma_superior += ancho * max(y_values[i], y_values[i + 1])
    
    error = abs(area_real, - (suma_inferior + suma_superior) / 2)

    return suma_inferior, suma_superior, abs, error

def graficar_funcion (a,b,c, intervalo_inicio, intervalo_fin, num_rectangulos. texto_resultado):
    x_plot = np.linspace (intervalo_inicio,intervalo_fin)
    y_plot = a * x**2