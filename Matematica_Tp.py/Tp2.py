import math

def distribucion_binomial(n, k, p):
    # Calcula el coeficiente binomial: nCk = n! / (k! * (n - k)!)
    coeficiente_binomial = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    
    # Calcula la probabilidad utilizando la fórmula de la distribución binomial
    probabilidad = coeficiente_binomial * (p**k) * ((1-p)**(n-k))
    return probabilidad

# Solicitar valores de n, k y p al usuario
n = int(input("Ingresa el número de ensayos (n): "))
k = int(input("Ingresa el número de éxitos deseados (k): "))
p = float(input("Ingresa la probabilidad de éxito en un ensayo (p): "))

# Calcular la distribución binomial
result = distribucion_binomial (n, k, p)

# Mostrar el resultado
print(f"La probabilidad de obtener exactamente {k} éxitos en {n} ensayos es: {result:.4f}")

def poisson_distribution(k, lam):

   # Calcula la probabilidad de obtener exactamente k eventos en una distribución de Poisson.

    #:param k: Número de eventos (entero no negativo).
    #:param lam: Tasa promedio de eventos (lambda).
    #:return: Probabilidad de obtener exactamente k eventos.
    # Calcular la probabilidad utilizando la fórmula de Poisson
    probability = (lam**k * math.exp(-lam)) / math.factorial(k)
    
    return probability

# Ejemplo de uso:
k = int(input("Ingresa el número de eventos (k) para calcular la distribucion poisson: "))
lam = float(input("Ingresa la tasa promedio de eventos (lambda): "))

# Calcular la distribución de Poisson
result = poisson_distribution(k, lam)

# Mostrar el resultado
print(f"La probabilidad de obtener exactamente {k} eventos es: {result:.4f}")

def distribucion_hipergeometrica (N, K, n, k):
 
    #Calcula la probabilidad hipergeométrica de obtener exactamente k éxitos en una muestra de tamaño n.

    
    # Cálculo del coeficiente binomial: math.comb(N, k) = N! / (k! * (N-k)!)
    distribucion_binomial(a, b):
    return math.comb(a, b)
    
    # Aplicar la fórmula de la distribución hipergeométrica
    probabilidad = (binomial_coefficient(K, k) * binomial_coefficient(N - K, n - k)) / binomial_coefficient(N, n)
    return probabilidad

def distribucion_normal(x, mu, sigma):
    coeficiente = 1 / (2 * math.pi * (sigma ** 2)) ** 0.5
    exponente = -((x - mu) ** 2) / (2 * sigma ** 2)
    densidad = coeficiente * math.exp(exponente)
    return densidad
# Solicitar datos al usuario
N = int(input("Ingresa el tamaño de la población total (N): "))
K = int(input("Ingresa el número total de éxitos en la población (K): "))
n = int(input("Ingresa el tamaño de la muestra (n): "))
k = int(input("Ingresa el número de éxitos deseados en la muestra (k): "))

# Calcular la distribución hipergeométrica
result = distribucion_hipergeometrica (N, K, n, k)

# Mostrar el resultado
print(f"La probabilidad de obtener exactamente {k} éxitos en una muestra de tamaño {n} es: {result:.4f}")