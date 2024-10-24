import numpy as np

# Función cuadrática general
def funcion_cuadratica(x, a, b, c):
    return a * x**2 + b * x + c

# Función para calcular las sumas inferior y superior
def calcular_sumas_inferior_superior(a, b, n, coef_a, coef_b, coef_c):
    # a y b son los límites del intervalo, n es el número de rectángulos
    # coef_a, coef_b, coef_c son los coeficientes de la función cuadrática ax^2 + bx + c

    delta_x = (b - a) / n  # Ancho de cada rectángulo
    suma_inferior = 0
    suma_superior = 0

    # Dividimos el intervalo en puntos
    x_values = np.linspace(a, b, n + 1)  # n+1 puntos para n rectángulos

    # Evaluamos la función en esos puntos
    y_values = [funcion_cuadratica(x, coef_a, coef_b, coef_c) for x in x_values]

    # Calculamos la suma inferior y superior
    for i in range(n):
        # Alturas en los extremos del intervalo
        altura_izquierda = y_values[i]
        altura_derecha = y_values[i+1]

        # Suma inferior: usamos la menor de las dos alturas
        suma_inferior += delta_x * min(altura_izquierda, altura_derecha)

        # Suma superior: usamos la mayor de las dos alturas
        suma_superior += delta_x * max(altura_izquierda, altura_derecha)

    return suma_inferior, suma_superior
