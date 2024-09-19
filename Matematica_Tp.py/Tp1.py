import math   
from collections import Counter
from scipy.integrate import quad

def calcular_mediana(lista):
    
    cantidad_lista = 0
    for numero in lista:
        if numero >= 0 or numero <= 0:
            cantidad_lista = len(lista)
        
    # Verifica si el número de lista es par o impar
    if cantidad_lista % 2 == 0:
        # Si es par, la mediana es el promedio de los dos valores del medio
        mediana = (lista[cantidad_lista//2 - 1] + lista[cantidad_lista // 2]) / 2
    else:
        # Si es impar, la mediana es el valor del medio
        mediana = lista[cantidad_lista//2]
    
    print(f"Estos son los datos ingresados: {lista}")
    return mediana

def calcular_moda(lista):
    # Crea un diccionario para contar la frecuencia de cada elemento
    frecuencia = {}
    lista = sorted(lista)
    for elemento in lista:
        if elemento in frecuencia:
            frecuencia[elemento] += 1 #le suma un valor de frecuencia al elemento encontrado si este ya fue encontrado antes
        else:
            frecuencia[elemento] = 1 #de lo contrario lo agrega y lo inicializa en cero
 
    # Encuentra el valor con la frecuencia más alta
    moda = max(frecuencia.values())
    
    
    # Creamos una lista para almacenar los elementos con la frecuencia más alta
    moda_resultado = []
    for key, value in frecuencia.items():
        if value == moda:
            moda_resultado.append(key)

    if moda == 1:
        print ("No hay una moda en estos datos")
        print (f"{moda_resultado}")
    else:
        print (f"esta es la moda de tus datos: {moda_resultado}")

    return moda_resultado  
 
def calcular_media (lista):

    #calcula la media y redondea su promedio
    media = round(sum(lista) / len(lista), 4)

    
    return media

def calcular_desviacion_estandar(lista): # como poblacion
    # Calcula la media

    media = int(sum (lista) / len(lista))
    
    # Suma el cuadrado de las diferencias con respecto a la media
    suma_cuadrados = sum((x - media) ** 2 for x in lista)
    
    # Divide entre el número de lista y calcular la raíz cuadrada
    desviacion_estandar = round(math.sqrt(suma_cuadrados / len(lista)), 2)

    

    return desviacion_estandar
 
def calcular_menor_mayor (lista):
    
    numeroMayor = lista[0]
    numeroMenor = lista[0]
    for numero in lista:
        if numero > numeroMayor:
            numeroMayor = numero
        if numero < numeroMenor:
            numeroMenor = numero
    print ("el dato menor es: ",numeroMenor)
    print ("el dato mayor es: ",numeroMayor)
    return numeroMenor,numeroMayor

def calcular_frecuencia_absoluta(lista):
    #Crea un diccionario de frecuencia para ubicar cada valor de frecuencia en la lista
    frecuencias = {}
    for valor in lista:
        if valor in frecuencias:
            frecuencias[valor] += 1 #le suma un valor de frecuencia al numero si ese numero ya existe en el diccionario
        else:
            frecuencias[valor] = 1 # de lo contrario lo inicializa en 1 
    return frecuencias 

def calcular_frecuencia_relativa(lista):
    
    total =  len(lista)
    frec_abs = calcular_frecuencia_absoluta(lista)
    frecuencia_rel = {}
    for clave, valor in frec_abs.items():
        frecuencia_rel[clave] = round(valor / total, 2)
    
    
    return frecuencia_rel

def calcular_varianza(lista):
    # Calcula la media
    media = int(sum(lista) / len(lista))
    # Suma el cuadrado de las diferencias con respecto a la media
    suma_cuadrados = round(sum((x - media) ** 2 for x in lista), 9)
    
    # Divide entre el número de datos que contiene la lista
    varianza = round(suma_cuadrados / len(lista), 2)
    print (f"Esta es la varianza de tus datos: {varianza:.2f}")
    return varianza

def calcular_frecuencia_porcentual(lista):
    # Crea un diccionario para contar la frecuencia absoluta de cada valor
    frecuencia_absoluta = calcular_frecuencia_relativa(lista)
    total_datos = len(lista)
    frecuencia_porcentual = {}
    for k, v in frecuencia_absoluta.items():
        frecuencia_porcentual [k] = round((v / total_datos) * 100, 2)

    return frecuencia_porcentual

def calcular_frecuencia_absoluta_acum(lista):
    frecuencia_absoluta = Counter(lista)
    acumulador = 0
    frecuencia_acum = {}
    for valor, frecuencia in frecuencia_absoluta.items():
        acumulador += frecuencia
        frecuencia_acum[valor] = acumulador
    
    print(f"Esta es tu frecuencia absoluta acumulada: {frecuencia_acum:}")
    return frecuencia_acum

def frecuencia_relativa_acum(lista):
    frecuencia_relativa = calcular_frecuencia_relativa(lista)
    acumulador = 0
    frecuenciarela_acum = {}
    for valor, frecuencia in frecuencia_relativa.items():
        acumulador += frecuencia
        frecuenciarela_acum[valor] = round(acumulador, 2)
    print(f"Esta es tu frecuencia relativa acumulada: {frecuenciarela_acum}")
    return frecuenciarela_acum

def calcular_frecuencia_porcentual_acum(lista):
    frecuencia_porcentual = calcular_frecuencia_porcentual(lista)
    acumulador = 0 
    frecuencia_porcentual_acum = {}
    for valor, frecuencia in frecuencia_porcentual.items():
        acumulador += frecuencia
        frecuencia_porcentual_acum[valor] = f"{round(acumulador, 2)}%"
    print (f"Esta es tu frecuencia porcentual acumulada: {frecuencia_porcentual_acum}")
    return frecuencia_porcentual_acum

def calcular_coeficiente_curtosis(lista):

    n = len(lista)  
    media = calcular_media(lista)
    desviacion = calcular_desviacion_estandar(lista)
        
    suma_cuarta_potencia = sum((x - media) ** 4 for x in lista)

    coeficiente_curtosis = (n * (n + 1) * suma_cuarta_potencia) / ((n - 1) * (n - 2) * (n - 3) * (desviacion ** 4)) \
               - (3 * (n - 1) ** 2) / ((n - 2) * (n - 3))
    
    
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
from math import comb, factorial, pi

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
    
    probabilidad = (lam**k * math.e ** (-lam)) / factorial(k)
    return probabilidad

# Distribución Hipergeométrica
def distribucion_hipergeometrica (N, K, n, x):
     
        # Calcula la probabilidad de una distribución hipergeométrica.
    
        #para N: Tamaño de la población.
        #para K: Número total de éxitos en la población.
        #para n: Tamaño de la muestra.
        #para x: Número de éxitos en la muestra.
        #return: Probabilidad de obtener exactamente k éxitos.
    
    probabilidad = (comb(K, x) * comb(N - K, n - x)) / comb(N, n)
    return probabilidad

# Distribución Gaussiana (Normal)
def distribucion_normal (x, mu, sigma):
    
    coeficiente = 1 / (2 * math.pi * (sigma ** 2)) ** 0.5
    exponente = -((x - mu) ** 2) / (2 * sigma ** 2)
    densidad = coeficiente * math.exp(exponente)
    return densidad

def calcular_integral(mu, sigma, primer_parametro, segundo_parametro):
    if primer_parametro > segundo_parametro:
        raise ValueError("El primer parámetro de integración debe ser menor o igual que el segundo")
    integral, error = quad(distribucion_normal, primer_parametro, segundo_parametro, args=(mu, sigma))
    return integral

def ingresar_datos():
    while True:
        try : 
            dato = input("Ingresa números separados por coma: ")
            dato_str = dato.split(',') 
            numeros = [int(numeros)for numeros in dato_str]
            numeros_ordenados = sorted(numeros)
            main_estadisticas(numeros_ordenados)
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
            
            
            if opcion == 15:
                return
            elif opcion == 1:
                print(f"Esta es la mediana de tus datos {calcular_mediana(numeros)}")
            elif opcion == 2:
                calcular_moda(numeros)
            elif opcion == 3:
                print (f"La media es {calcular_media(numeros):.2}")
            elif opcion == 4:
                calcular_menor_mayor(numeros)
            elif opcion == 5:
                calcular_varianza(numeros)
            elif opcion == 6:
                print (f"Tu desviacion estandar es {calcular_desviacion_estandar(numeros)}")
            elif opcion == 7:
                print (f"Esta es tu frecuencia absoluta: {calcular_frecuencia_absoluta(numeros)}")
            elif opcion == 8: 
                print(f"Esta es la frecuencia relativa de tus datos: {calcular_frecuencia_relativa(numeros)}")
            elif opcion == 9 :
                print (f"Esta es la frecuencia porcentual de tus datos {calcular_frecuencia_porcentual(numeros)}")
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
                if sigma <= 0:
                    raise ValueError("La desviación estándar debe ser mayor que 0")
                tipo_distribucion = input("¿Desea calcular la probabilidad para x menor que infinito o x mayor que infinito? (escriba menor que o mayor que): ")
                
                if tipo_distribucion == "menor que":
                        resultado = calcular_integral(mu, sigma, -float('inf'), x)
                        print(f"La probabilidad gaussiana (densidad) en {x} es: {resultado:.2f}%")
    
                elif tipo_distribucion == "mayor que":
                        resultado = calcular_integral(mu, sigma, x, float('inf'))
                        print(f"La probabilidad gaussiana (densidad) en {x} es: {resultado:.2f}%")
                else:
                    raise ValueError("Opción de distribución no válida.")
            
            elif opcion == 5: 
                return
        
            else:
                print("Opción no válida. Por favor, selecciona una opción entre 1 y 5.")
        except ValueError as e:
            print(f"Error: {e}")
    
        except KeyboardInterrupt:
            print("\nSaliendo del menú de distribuciones...")

if __name__ == "__main__":
    main()
