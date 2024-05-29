def calcular_mediana(datos):
    # Ordenar los datos
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    
    # Verificar si el número de datos es par o impar
    if n % 2 == 0:
        # Si es par, la mediana es el promedio de los dos valores del medio
        mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
    else:
        # Si es impar, la mediana es el valor del medio
        mediana = datos_ordenados[n//2]
    
    return mediana
def calcular_moda(lista):
    # Creamos un diccionario para contar la frecuencia de cada elemento
    frecuencia = {}
    for elemento in lista:
        if elemento in frecuencia:
            frecuencia[elemento] += 1 #le suma un valor de frecuencia al elemento encontrado si este ya fue encontrado antes
        else:
            frecuencia[elemento] = 1 # de lo contrario si hay solo uno inicializa en base 1 y si se repite se sigue sumando su frecuencia
    
    # Encontramos el valor con la frecuencia más alta
    moda = max(frecuencia.values())
    
    # Creamos una lista para almacenar los elementos con la frecuencia más alta
    moda_resultado = []
    for key, value in frecuencia.items():
        if value == moda:
            moda_resultado.append(key)
    
    return moda_resultado   
def solicitar_datos():
    lista = []
    while True:
        dato = input("Ingresa un número entero (o 'listo' para terminar): ")
        if dato.lower() == 'listo':
            break
        elif dato.lower() == float:
            numero = float(dato)
            lista.append(numero)
        else:
            print("por favor ingresa un numero entero ")
    return lista    
