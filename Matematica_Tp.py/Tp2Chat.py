
import math
from math import comb, exp, factorial, sqrt, pi

# Distribución Binomial
def distribucion_binomial(n, k, p):
    
    # Calcula la probabilidad de una distribución binomial.
    
    coeficiente_binomial = comb(n, k)
    probabilidad = coeficiente_binomial * (p**k) * ((1-p)**(n-k))
    return probabilidad

# Distribución de Poisson
def distribucion_poisson (k, lam):
    
    # Calcula la probabilidad de una distribución de Poisson.
    
    #param k: Número de exitos.
    #param lam: Tasa promedio de exitos (lambda).
    #return: Probabilidad de obtener exactamente k eventos.
    
    probabilidad = (lam**k * exp(-lam)) / factorial(k)
    return probabilidad

# Distribución Hipergeométrica
def distribucion_hipergeometrica (N, K, n, k):
     
        # Calcula la probabilidad de una distribución hipergeométrica.
    
        #para N: Tamaño de la población.
        #para K: Número total de éxitos en la población.
        #para n: Tamaño de la muestra.
        #para k: Número de éxitos en la muestra.
        #return: Probabilidad de obtener exactamente k éxitos.
    
    probabilidad = (comb(K, k) * comb(N - K, n - k)) / comb(N, n)
    return probabilidad

# Distribución Gaussiana (Normal)
def distribucion_normal (x, mu, sigma):
    
    # Calcula la función de densidad de probabilidad de una distribución normal.

    probabilidad = (1 / (sigma * sqrt(2 * pi))) * exp(-0.5 * ((x - mu) / sigma) ** 2)
    return probabilidad

# Menú para seleccionar la distribución

def main():
        print("Selecciona la distribución a calcular:")
        print("1. Distribución Binomial")
        print("2. Distribución de Poisson")
        print("3. Distribución Hipergeométrica")
        print("4. Distribución Normal")    
        print("5. Salir")    
while True:
        
        try:
            main()
            opcion = int(input("Ingresa el número de la distribución que deseas usar: "))
            
            if opcion == 1:
            # Distribución Binomial
                n = int(input("Ingresa el número de ensayos (n): "))
                k = int(input("Ingresa el número de éxitos (k): "))
                p = float(input("Ingresa la probabilidad de éxito en un ensayo (p): "))
                resultado = distribucion_binomial(n, k, p)
                print(f"La probabilidad binomial de obtener exactamente {k} éxitos en {n} ensayos es: {resultado:.4f}")

            elif opcion == 2:
                # Distribución de Poisson
                k = int(input("Ingresa el número de exitos (k): "))
                lam = float(input("Ingresa la tasa promedio de exitos (lambda): ")) 
                resultado = distribucion_poisson(k, lam)
                print(f"La probabilidad de Poisson de obtener exactamente {k} eventos es: {resultado:.4f}")

            elif opcion == 3:
                # Distribución Hipergeométrica
                N = int(input("Ingresa el tamaño de la población total (N): "))
                K = int(input("Ingresa el número total de éxitos en la población (K): "))
                n = int(input("Ingresa el tamaño de la muestra (n): "))
                k = int(input("Ingresa el número de éxitos en la muestra (k): "))
                resultado = distribucion_hipergeometrica(N, K, n, k)
                print(f"La probabilidad hipergeométrica de obtener exactamente {k} éxitos en una muestra de tamaño {n} es: {resultado:.4f}")

            elif opcion == 4:
                #Distribución Normal
                x = float(input("Ingresa el valor a evaluar (x): "))
                mu = float(input("Ingresa la media (mu): "))
                sigma = float(input("Ingresa la desviación estándar (sigma): "))
                resultado = distribucion_normal(x, mu, sigma)
                print(f"La probabilidad gaussiana (densidad) en {x} es: {resultado:.2f}%")

            elif opcion == 5: 
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción entre 1 y 5.")

        except ValueError():
            print ("Dato ingresado no valido")

