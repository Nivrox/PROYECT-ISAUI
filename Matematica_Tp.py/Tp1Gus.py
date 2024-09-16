def calcular_mediana(lista):
    # Ordenar los elementos de la lista
    lista_ordenada = sorted(lista)
    print(lista_ordenada)
    cantidad_lista = 0
    for numero in lista:
        if numero >= 0 or numero <= 0:
            cantidad_lista = len(lista_ordenada)
        
    # Verificar si el número de lista es par o impar
    if cantidad_lista % 2 == 0:
        # Si es par, la mediana es el promedio de los dos valores del medio
        mediana = (lista_ordenada[cantidad_lista//2 - 1] + lista_ordenada[cantidad_lista // 2]) / 2
    else:
        # Si es impar, la mediana es el valor del medio
        mediana = lista_ordenada[cantidad_lista//2]
    print("Esta es la mediana de tu lista : ", mediana)
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
    print ("Esta es la moda de tus datos: ", moda_resultado)
    return moda_resultado   
def calcular_media (lista):

    media = sum(lista) / len(lista)

    print("La media es: ", media)
    cantidad_lista = len(lista)
    print("La cantidad de datos ingresados fueron: ",cantidad_lista) 
def calcular_minimo_mayor (lista):
    numeroMayor = lista [0]
    numeroMenor = lista [0]
    for numero in lista:
        if numero > numeroMayor:
            numeroMayor = numero
        if numero < numeroMenor:
            numeroMenor = numero
    print ("El dato minimo es: ",numeroMenor)
    print ("El dato mayor es: ",numeroMayor)
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


while True:
    try :
        dato = input("Ingresa números separados por coma: ")
        dato_str = dato.split(',')
        numeros = [float(numeros)for numeros in dato_str]
        break
        
    except ValueError:
        print ("Dato no admitido por favor ingresa los lista con coma ")
        print("Ejemplo : '1,2,3,4,7' ")    
        
while True: 
        
    try:
        usuario = input ("Que dato desea ver Mediana, Moda, Media, Mayor y Minimo, Cuartiles, Frecuencia o Todos:")
        if usuario.lower() == "mediana":    
            calcular_mediana (numeros)
        if usuario.lower() == "moda": 
            calcular_moda(numeros)
        if usuario.lower () == "media":
            calcular_media(numeros)
        if usuario.lower () == "mayor y menor":
            calcular_minimo_mayor(numeros)
        if usuario.lower() == "cuartiles":
            calcular_cuartiles(numeros)
        if usuario.lower() == "frecuencia":
            calcular_frecuencia_absoluta (numeros)
        elif usuario.lower() == "todos":
            calcular_mediana (numeros)
            calcular_moda(numeros)
            calcular_media(numeros)
            calcular_cuartiles(numeros)
            calcular_minimo_mayor(numeros)
            calcular_frecuencia_absoluta(numeros)
            print(numeros)
        if usuario.lower() == "volver":
            break
        else:
            False
    except ValueError:
            print ("Ingrese de nuevo su consulta")
while True:
    try :
        dato = input("Ingresa números separados por coma: ")
        dato_str = dato.split(',')
        numeros = [float(numeros)for numeros in dato_str]
        break
    except ValueError:
        print ("dato no admitido por favor ingresa los lista con coma ")
        print("ejemplo : '1,2,3,4,7' ")    
        
while True: 
        
    try:
        usuario = input ("Que dato desea ver Mediana, Moda, Media, Mayor y Minimo, Cuartiles, Frecuencia o todos:")
        if usuario.lower() == "mediana":    
            calcular_mediana (numeros)
        if usuario.lower() == "moda": 
            calcular_moda(numeros)
        if usuario.lower () == "media":
            calcular_media(numeros)
        if usuario.lower () == "mayor y menor":
            calcular_minimo_mayor(numeros)
        if usuario.lower() == "cuartiles":
            calcular_cuartiles(numeros)
        if usuario.lower() == "frecuencia":
            calcular_frecuencia_absoluta (numeros)
        elif usuario.lower() == "todos":
            calcular_mediana (numeros)
            calcular_moda(numeros)
            calcular_media(numeros)
            calcular_cuartiles(numeros)
            calcular_minimo_mayor(numeros)
        if usuario.lower() == "volver":
            break
        else:
            False
    except ValueError:
            print ("ingrese de nuevo su consulta")
while True:
    try :
        dato = input("Ingresa números separados por coma: ")
        dato_str = dato.split(',')
        numeros = [float(numeros)for numeros in dato_str]
        break
    except ValueError:
        print ("dato no admitido por favor ingresa los lista con coma ")
        print("ejemplo : '1,2,3,4,7' ")    
        
while True: 
        
    try:
        usuario = input ("Que dato desea ver Mediana, Moda, Media, Mayor y Minimo, Cuartiles, Frecuencia o todos:")
        if usuario.lower() == "mediana":    
            calcular_mediana (numeros)
        if usuario.lower() == "moda": 
            calcular_moda(numeros)
        if usuario.lower () == "media":
            calcular_media(numeros)
        if usuario.lower () == "mayor y menor":
            calcular_minimo_mayor(numeros)
        if usuario.lower() == "cuartiles":
            calcular_cuartiles(numeros)
        if usuario.lower() == "frecuencia":
            calcular_frecuencia_absoluta (numeros)
        if usuario.lower() == "todos":
            calcular_mediana (numeros)
            calcular_moda(numeros)
            calcular_media(numeros)
            calcular_cuartiles(numeros)
            calcular_minimo_mayor(numeros)
            calcular_cuartiles(numeros)
            break
        if usuario.lower() == "volver":
           break
        else:
            print ("ingrese de nuevo su consulta") 
    except ValueError:
            print ("ingrese de nuevo su consulta")