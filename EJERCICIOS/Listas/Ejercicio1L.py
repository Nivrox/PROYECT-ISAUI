def suma_elementos_lista(lista):
    if not lista:
        print ("no hay datos dentro de la lista")
    else:
        suma = 0 
        for numero in lista:
            suma += numero

    return suma


datosEntrada = input ("ingresa los numeros separados por coma")
numeros_str = datosEntrada.split(',')   
numero = [int(numero) for numero in numeros_str]    
print ("este es el resultado: ",suma_elementos_lista(numero))
   