import math
def calcular_mediana(lista):
    # Ordenar los lista
    cantidad_lista = 0
    for numero in lista:
        if numero >= 0 or numero <= 0:
            cantidad_lista = len(lista)
        
    # Verificar si el número de lista es par o impar
    if cantidad_lista % 2 == 0:
        # Si es par, la mediana es el promedio de los dos valores del medio
        mediana = (lista[cantidad_lista//2 - 1] + lista[cantidad_lista // 2]) / 2
    else:
        # Si es impar, la mediana es el valor del medio
        mediana = lista[cantidad_lista//2]
    print("Esta es la mediana de tus lista : ", mediana)
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
    print ("esta es la moda de tus lista: ", moda_resultado)
    return moda_resultado   
def calcular_media (lista):

    media = sum(lista) / len(lista)

    print("La media es: ", media)
    cantidad_lista = len(lista)
    print("Cantidad de lista ingresados fueron: ",cantidad_lista) 
def calcular_minimo (lista):
    numeroMayor = lista [0]
    numeroMenor = lista [0]
    for numero in lista:
        if numero > numeroMayor:
            numeroMayor = numero
        if numero < numeroMenor:
            numeroMenor = numero
    print ("el dato minimo es: ",numeroMenor)
    print ("el dato mayor es: ",numeroMayor)
    return numeroMenor,numeroMayor
def calcular_cuartiles(lista):
    
    n = len(lista)
    
    Q2 = (lista[n // 2 - 1] + lista[n // 2]) / 2 if n % 2 == 0 else lista[n // 2]
    
    mitad = n // 2
    Q1 = (lista[mitad // 2 - 1] + lista[mitad // 2]) / 2 if mitad % 2 == 0 else lista[mitad // 2]
    
    if n % 2 == 0:
        Q3 = (lista[mitad + mitad // 2 - 1] + lista[mitad + mitad // 2]) / 2 if mitad % 2 == 0 else lista[mitad + mitad // 2]
    else:
        Q3 = (lista[mitad + 1 + mitad // 2 - 1] + lista[mitad + 1 + mitad // 2]) / 2 if (mitad + 1) % 2 == 0 else lista[mitad + 1 + mitad // 2]
    print ("Q1 vale:",Q1,", q2 vale:",Q2,"y q3 vale: ",Q3)
    return Q1, Q2, Q3
def calcular_frecuencia_absoluta(lista):
    frecuencias = {}
    for valor in lista:
        if valor in frecuencias:
            frecuencias[valor] += 1
        else:
            frecuencias[valor] = 1
def calcular_frecuencia_relativa(lista):
    frecuencias_absolutas = calcular_frecuencia_absoluta(lista)
    total_elementos = len(lista)
    frecuencias_relativas = {valor: frecuencia / total_elementos for valor, frecuencia in frecuencias_absolutas.items()}
    return frecuencias_relativas
def calcular_frecuencia_absoluta_acumulada(lista):
    frecuencias_absolutas = calcular_frecuencia_absoluta(lista)
    # Ordenar los datos dentro de la lista por clave (valor)
    valores_ordenados = sorted(frecuencias_absolutas.keys())
    frecuencias_acumuladas = {}
    acumulador = 0
    for valor in valores_ordenados:
        acumulador += frecuencias_absolutas[valor]
        frecuencias_acumuladas[valor] = acumulador
    return frecuencias_acumuladas
def calcular_frecuencia_relativa_acumulada(lista):
    frecuencias_relativas = calcular_frecuencia_relativa(lista)
    valores_ordenados = sorted(frecuencias_relativas.keys())
    frecuencias_acumuladas = {}
    acumulador = 0
    for valor in valores_ordenados:
        acumulador += frecuencias_relativas[valor]
        frecuencias_acumuladas[valor] = acumulador
    return frecuencias_acumuladas
def calcular_porcentaje(lista):
    frecuencias_absolutas = calcular_frecuencia_absoluta(lista)
    total_elementos = len(lista)
    porcentajes = {valor: (frecuencia / total_elementos) * 100 for valor, frecuencia in frecuencias_absolutas.items()}
    return porcentajes
def calcular_porcentaje_acumulado(lista):
    porcentajes = calcular_porcentaje(lista)
    valores_ordenados = sorted(porcentajes.keys())
    porcentajes_acumulados = {}
    acumulador = 0
    for valor in valores_ordenados:
        acumulador += porcentajes[valor]
        porcentajes_acumulados[valor] = acumulador
    return porcentajes_acumulados
def calcular_desviacion_absoluta_y_estandar(lista):
    media = calcular_media(lista)

    desviacion_absoluta = sum(map(lambda x: abs(x - sum(lista)/len(lista)), lista)) / len(lista)
    print("Desviación absoluta:", desviacion_absoluta)
    desviacion_estandar = math.sqrt(sum(map(lambda x: (x - sum(lista)/len(lista))**2, lista)) / len(lista))
    print("Desviación estándar:", desviacion_estandar)
    return desviacion_absoluta, desviacion_estandar
while True:
    try :
        
        dato = input("Ingresa números separados por coma: ")
        dato_str = dato.split(',')
        numeros = [float(numeros)for numeros in dato_str]
        calcular_mediana (numeros)
        calcular_moda(numeros)
        calcular_media(numeros)
        calcular_minimo(numeros)
        calcular_cuartiles(numeros)
        calcular_desviacion_absoluta_y_estandar(numeros)
        break
    except ValueError:
        print ("dato no admitido por favor ingresa los lista con coma ")
        print("ejemplo : '1,2,3,4,7' ")