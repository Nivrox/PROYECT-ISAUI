def promedio_lista (lista):
    numero = [0]
    suma = 0
    for numero in lista:
        suma += numero
    cantidad = len(lista)
    promedio = suma / cantidad
    return promedio


while True:
    datos = input ("Ingresa los datos separados por coma: ")
    try:    
        datos_str = datos.split(',')    
        numeros = [int(numeros)for numeros in datos_str]
        print ("este es tu promedio :", promedio_lista(numeros))
        break
    except ValueError:
        print ("ingresa datos numericos por favor")