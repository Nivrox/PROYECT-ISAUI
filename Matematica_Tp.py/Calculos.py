import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Definir las diferentes funciones disponibles
def f_polinomica(x):
    return 3*x**3 - 2*x**2 + x
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Definir las diferentes funciones disponibles
def f_polinomica(x):
    return 3*x**3 - 2*x**2 + x

def f_seno(x):
    return np.sin(x)

def f_coseno(x):
    return np.cos(x)

def f_exponencial(x):
    return np.exp(x)

def f_logaritmica(x):
    return np.log(x)

# Solicitar al usuario que elija la función
print("Seleccione una función para calcular el área bajo la curva:")
print("1. Función polinómica: 3x^3 - 2x^2 + x")
print("2. Función seno: sin(x)")
print("3. Función coseno: cos(x)")
print("4. Función exponencial: e^x")
print("5. Función logarítmica: ln(x) (requiere x > 0)")

opcion = int(input("Ingrese el número de la función elegida: "))

# Asignar la función seleccionada
if opcion == 1:
    f = f_polinomica
    label_funcion = "f(x) = 3x^3 - 2x^2 + x"
elif opcion == 2:
    f = f_seno
    label_funcion = "f(x) = sin(x)"
elif opcion == 3:
    f = f_coseno
    label_funcion = "f(x) = cos(x)"
elif opcion == 4:
    f = f_exponencial
    label_funcion = "f(x) = e^x"
elif opcion == 5:
    f = f_logaritmica
    label_funcion = "f(x) = ln(x)"
else:
    raise ValueError("Opción no válida. Por favor, selecciona un número entre 1 y 5.")

# Solicitar los límites del intervalo y el número de rectángulos
a = float(input("Ingrese el límite inferior del intervalo: "))
b = float(input("Ingrese el límite superior del intervalo: "))
n = int(input("Ingrese el número de rectángulos: "))

# Validar que el intervalo sea adecuado para la función logarítmica
if opcion == 5 and a <= 0:
    raise ValueError("Para la función logarítmica, el límite inferior debe ser mayor que 0.")

# Calcular el ancho de cada rectángulo
delta_x = (b - a) / n

# Inicializar las sumas
sum_inferior = 0
sum_superior = 0

# Calcular las sumas inferior y superior
for i in range(n):
    # Suma inferior: usar el extremo izquierdo
    sum_inferior += f(a + i * delta_x) * delta_x
    # Suma superior: usar el extremo derecho
    sum_superior += f(a + (i + 1) * delta_x) * delta_x

# Calcular el área real usando integración numérica
area_real, _ = quad(f, a, b)

# Crear la gráfica
x_plot = np.linspace(a, b, 100)
y_plot = f(x_plot)

plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot, label=label_funcion, color='blue')

# Dibujar los rectángulos para la suma inferior
for i in range(n):
    plt.bar(a + i * delta_x, f(a + i * delta_x), width=delta_x, alpha=0.3, align='edge', color='blue', edgecolor='black')

# Dibujar los rectángulos para la suma superior (usando un color diferente, por ejemplo, verde)
for i in range(n):
    plt.bar(a + (i + 1) * delta_x, f(a + (i + 1) * delta_x), width=-delta_x, alpha=0.3, align='edge', color='red', edgecolor='black')

# Mostrar los resultados en la gráfica
plt.text(a + (b - a) / 2, max(y_plot) * 0.8, 
         f"Suma Inferior: {sum_inferior:.4f}\nSuma Superior: {sum_superior:.4f}\nÁrea Real: {area_real:.4f}", 
         fontsize=12, ha='center', bbox=dict(facecolor='white', alpha=0.7))

plt.title('Suma Inferior y Superior bajo la curva')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(a, b)
plt.ylim(0, max(y_plot) * 1.1)
plt.legend()
plt.grid(True)
plt.show()
