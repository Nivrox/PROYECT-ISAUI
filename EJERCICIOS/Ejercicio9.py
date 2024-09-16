#Crear una calculadora de numeros factoriales positivos

def factoriales_iterativo (n):

    if n < 0:
        return "no definido para numeros negativos"
    resultado = 1
    for i in range (1, n + 1):
        resultado *= i 
    return resultado
print ("Que onda soy una calculadora de factoriales amio")

dato = input ("Ingresa tu numero a calcular : ") 
if dato.isdigit():
    numero = int(dato)
    factorial = factoriales_iterativo(numero)
    print ("el factorial de", numero, "es : ", factorial)
else:
        numero = int (dato)
        factorial = factoriales_iterativo(numero)
        print (factorial)
        print ("Ingresa numeros enteros ")    