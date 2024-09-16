import math 
from math import comb, exp, factorial, sqrt, pi 
import statistics

def calcular_mediana1(lista):
    lista_ordenada = sorted(lista)
    return  round(statistics.median(lista_ordenada))


dato = input("Ingresa números separados por coma: ")
dato_str = dato.split(',')
numeros = [float(numeros)for numeros in dato_str]
calcular_mediana1(numeros)
print (f"La mediana es {calcular_mediana1}")