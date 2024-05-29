def numero_mayor_lista(lista):
    numero = lista[0]
    numeroMayor = []
    elemento = 7
    numerosMenores = 0
    for numero in lista:
        if numero > elemento:
            numeroMayor.append(numero)
        else:
            numerosMenores = numero
    print ("Estos son los numeros mayor a 7:")
    for numero in numeroMayor:
        
        print (numero)
    return numeroMayor


while True:
    try:
        datos = input ("Ingresa numeros separados por coma: ")
        datos_str = datos.split(',')
        numero = [float(numero)for numero in datos_str]
        print (numero_mayor_lista(numero))
        break
    except ValueError:
        print ("dato no recibido por favor ingresa solo numeros separados por coma")