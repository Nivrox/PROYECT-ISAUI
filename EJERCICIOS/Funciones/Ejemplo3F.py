import math
def calcular_area_perimetro(radio, diametro):
 
    
    pi = 3.1416
    if radio >= 0 :
        area = pi * (radio **2)
    if diametro >= 0 :
        perimetro = pi * diametro
    else: 
        pass 
    print ("El area de tu cicunferencia es: ", area)
    print ("este es tu perimetro: ", perimetro)
    return area, perimetro

radio = float(input("Pon la longitud de radio en tu circunferencia: "))
diametro = float (input("Pon el diametro en tu circunferencia para calcular su perimetral: "))
#radio = 5
#diametro = 10
calcular_area_perimetro(radio, diametro)