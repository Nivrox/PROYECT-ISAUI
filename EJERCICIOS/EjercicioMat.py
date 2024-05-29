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

datos_ordenados = float(input("Ingrese Los Datos Correspondientes"))
if datos_ordenados >= 0:
# Ejemplo de uso

    print("La mediana es:", calcular_mediana(datos_ordenados)) 
else:
    print ("los datos ingresados no son correctos")