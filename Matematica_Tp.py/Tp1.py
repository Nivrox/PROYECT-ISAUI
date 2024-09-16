import math
from math import sqrt    
from collections import Counter
from scipy.stats import kurtosis




def calcular_mediana(lista):
    # Ordenar los lista
    lista_ordenada = sorted(lista)
    cantidad_lista = 0
    for numero in lista_ordenada:
        if numero >= 0 or numero <= 0:
            cantidad_lista = len(lista_ordenada)
        
    # Verificar si el número de lista es par o impar
    if cantidad_lista % 2 == 0:
        # Si es par, la mediana es el promedio de los dos valores del medio
        mediana = (lista_ordenada[cantidad_lista//2 - 1] + lista_ordenada[cantidad_lista // 2]) / 2
    else:
        # Si es impar, la mediana es el valor del medio
        mediana = lista_ordenada[cantidad_lista//2]
    print(f"Esta es la mediana de tu lista : {mediana}")
    print(f"Estos son los datos ingresados: {lista_ordenada}")
    return mediana

def calcular_moda(lista):
    # Creamos un diccionario para contar la frecuencia de cada elemento
    frecuencia = {}
    for elemento in lista:
        if elemento in frecuencia:
            frecuencia[elemento] += 1 #le suma un valor de frecuencia al elemento encontrado si este ya fue encontrado antes
        else:
            frecuencia[elemento] = 1 #de lo contrario lo agrega y lo inicializa en cero
 
    # Encontramos el valor con la frecuencia más alta
    moda = max(frecuencia.values())
    
    # Creamos una lista para almacenar los elementos con la frecuencia más alta
    moda_resultado = []
    for key, value in frecuencia.items():
        if value == moda:
            moda_resultado.append(key)
    print ("esta es la moda de tus datos: ", moda_resultado)

    return moda_resultado  
 
def calcular_media (lista):

    media = sum(lista) / len(lista)

    print("La media es: ", media)
    return media

def calcular_desviacion_estandar(lista): # como poblacion
    # Calcular la media
    media = sum (lista) / len(lista)
    
    # Sumar el cuadrado de las diferencias con respecto a la media
    suma_cuadrados = sum((x - media) ** 2 for x in lista)
    
    # Dividir entre el número de lista y calcular la raíz cuadrada
    desviacion_estandar = math.sqrt(suma_cuadrados / len(lista))

    print (f"Tu desviacion estandar es: {desviacion_estandar}")

    return desviacion_estandar
 
def calcular_menor_mayor (lista):
    numeroMayor = lista [0]
    numeroMenor = lista [0]
    for numero in lista:
        if numero > numeroMayor:
            numeroMayor = numero
        if numero < numeroMenor:
            numeroMenor = numero
    print ("el dato menor es: ",numeroMenor)
    print ("el dato mayor es: ",numeroMayor)
    return numeroMenor,numeroMayor

def calcular_frecuencia_absoluta(lista):
    frecuencias = {}
    for valor in lista:
        if valor in frecuencias:
            frecuencias[valor] += 1
        else:
            frecuencias[valor] = 1

    print ("Esta es tu frecuencia absoluta",frecuencias)
    return frecuencias 

def calcular_frecuencia_relativa(lista):
    total =  len(lista)
    frec_abs = calcular_frecuencia_absoluta(lista)
    frecuencia_rel = {}
    for clave, valor in frec_abs.items():
        frecuencia_rel[clave] = round(valor / total, 4)
    
    print("Esta es la frecuencia relativa de tus datos", frecuencia_rel)
    return frecuencia_rel

def calcular_varianza(lista):
    # Calcular la media
    media = sum(lista) / len(lista)
    
    # Sumar el cuadrado de las diferencias con respecto a la media
    suma_cuadrados = sum((x - media) ** 2 for x in lista)
    
    # Dividir entre el número de lista
    varianza = round(suma_cuadrados / len(lista), 4)
    print (f"Esta es la varianza de tus datos: {varianza}")
    return varianza

def calcular_frecuencia_porcentual(lista):
    # Crea un diccionario para contar la frecuencia absoluta de cada valor
    frecuencia_absoluta = calcular_frecuencia_absoluta(lista)
    total_datos = len(lista)
    frecuencia_porcentual = {k: (v / total_datos) * 100 for k, v in frecuencia_absoluta.items()}
    print (f"Esta es la frecuencia porcentual de tus datos {frecuencia_porcentual}")
    return frecuencia_porcentual

def calcular_frecuencia_absoluta_acum(lista):
    frecuencia_absoluta = Counter(sorted(lista))
    acumulador = 0
    frecuencia_acum = {}
    for valor, frecuencia in frecuencia_absoluta.items():
        acumulador += frecuencia
        frecuencia_acum[valor] = acumulador
        return frecuencia_acum

def frecuencia_relativa_acum(lista):
    frecuencia_relativa = calcular_frecuencia_relativa(sorted(lista))
    acumulador = 0
    frecuenciarela_acum = {}
    for valor, frecuencia in frecuencia_relativa.items():
        acumulador += frecuencia
        frecuenciarela_acum[valor] = round(acumulador, 4)
    print(f"Esta es tu frecuencia relativa acumulada: {frecuenciarela_acum}")
    return frecuenciarela_acum

def calcular_frecuencia_porcentual_acum(lista):
    frecuencia_porcentual = calcular_frecuencia_porcentual(sorted(lista))
    acumulador = 0 
    frecuencia_porcentual_acum = {}
    for valor, frecuencia in frecuencia_porcentual.items():
        acumulador += frecuencia
        frecuencia_porcentual_acum[valor] = f"{round(acumulador, 4)}%"
    return frecuencia_porcentual_acum

def calcular_coeficiente_curtosis(lista):

    coeficiente_curtosis = kurtosis(lista)
    
    
    if coeficiente_curtosis == 0:
        print(f"tu coeficiente curtosis vale {coeficiente_curtosis} y La distribución es mesocúrtica")
        interpretación= f"tu coeficiente curtosis vale {coeficiente_curtosis} y La distribución es mesocúrtica"
    if coeficiente_curtosis > 0:
        print(f"tu coeficiente curtosis vale {coeficiente_curtosis} y La distribución es leptocúrtica")
        interpretación= f"tu coeficiente curtosis vale {coeficiente_curtosis} y La distribucion es leptocúrtica"
    if coeficiente_curtosis < 0:
        print(f"tu coeficiente curtosis vale {coeficiente_curtosis} y La distribución es platicúrtica")
        interpretación= f"tu coeficiente curtosis vale {coeficiente_curtosis} y La distribucion es platicúrtica"
        
    
    return interpretación 


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

def ingresar_datos():
    while True:
        try : 
            dato = input("Ingresa números separados por coma: ")
            dato_str = dato.split(',')
            numeros = [int(numeros)for numeros in dato_str]
            main_estadisticas(numeros)
            break
            
        except ValueError:
            print ("dato no admitido por favor ingresa los lista con coma ")
            print("ejemplo : '1,2,3,4,7' ")    

def main_estadisticas(numeros):
    while True: 
        try:
            print("1. Mediana")
            print("2. Moda")
            print("3. Media")
            print("4. Mayor y Mínimo")
            print("5. Varianza")
            print("6. Desviacion estandar")
            print("7. Frecuencia Absoluta")
            print("8. Frecuencia Relativa")
            print("9. Frecuencia Porcentual")
            print("10. Frecuencia Absoluta Acumulada")
            print("11. Frecuencia Relativa Acumulada")
            print("12. Frecuencia Porcentual Acumulada")
            print("13. Coeficiente Curtosis")
            print("14. Todos")
            print("15. Volver al menú principal")
            
            opcion = input("¿Qué dato desea ver?: ")
            
            # Validar si la opción es un número
            try:
                opcion = int(opcion)
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue  # Reinicia el ciclo si el input no es válido
            
            
            if opcion == 1:
                calcular_mediana(numeros)
            elif opcion == 2:
                calcular_moda(numeros)
            elif opcion == 3:
                calcular_media(numeros)
            elif opcion == 4:
                calcular_menor_mayor(numeros)
            elif opcion == 5:
                calcular_varianza(numeros)
            elif opcion == 6:
                calcular_desviacion_estandar(numeros)
            elif opcion == 7:
                calcular_frecuencia_absoluta(numeros)
            elif opcion == 8: 
                calcular_frecuencia_relativa(numeros)
            elif opcion == 9 :
                calcular_frecuencia_porcentual(numeros)
            elif opcion == 10: 
                calcular_frecuencia_absoluta_acum (numeros)
            elif opcion == 11:
                frecuencia_relativa_acum(numeros)
            elif opcion == 12:
                calcular_frecuencia_porcentual_acum(numeros)
            elif opcion == 13:
                calcular_coeficiente_curtosis(numeros)
            elif opcion == 14:
                calcular_mediana(numeros)
                calcular_moda(numeros)
                calcular_media(numeros)
                calcular_menor_mayor(numeros)
                calcular_varianza(numeros)
                calcular_desviacion_estandar(numeros)
                calcular_frecuencia_absoluta(numeros)
                calcular_frecuencia_relativa(numeros)
                calcular_frecuencia_porcentual(numeros)
                calcular_frecuencia_absoluta_acum(numeros)
                frecuencia_relativa_acum(numeros)
                calcular_frecuencia_porcentual_acum(numeros)    
                calcular_coeficiente_curtosis(numeros)
            elif opcion == 15:
                return  # Salir del menú estadistico

            else:
                print(f"Opción {opcion} no válida.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
def main():
        while True:
            try:
                print("\nMenú Principal:")
                print("A. Cálculos Estadísticos")
                print("B. Cálculos de Distribuciones")
                print("0. Salir")

                opcion_principal = input("Ingrese la opción que desea seleccionar: ").upper()

                if opcion_principal == "0":
                    print("Saliendo...")
                    break
                elif opcion_principal == "A":
                    numeros = ingresar_datos()
                    main_estadisticas (numeros)
                elif opcion_principal == "B":
                    menu_distribuciones()
                else:
                    print("Opción no válida. Intente nuevamente.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número válido.")
def menu_distribuciones():
       
    while True:
        
        try:
            print("Selecciona la distribución a calcular:")
            print("1. Distribución Binomial")
            print("2. Distribución de Poisson")
            print("3. Distribución Hipergeométrica")
            print("4. Distribución Normal")    
            print("5. Menu principal")   
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
                return
            else:
                print("Opción no válida. Por favor, selecciona una opción entre 1 y 5.")

        except ValueError():
            print ("Dato ingresado no valido")

if __name__ == "__main__":
    main()
