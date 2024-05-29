#Desarrolla un programa en Python que solicite al usuario que ingrese una frase 
#y luego cuente y muestre el número de palabras en esa frase.
def contar_caracter (cadena):
    caracter = 0
    for i in cadena:
        if i.isalpha or i.isdigit():
         caracter = caracter + 1
        else:
           pass
    return caracter
texto = input ("ingrese un texto ")
resultado = contar_caracter (texto)
print ("Cantidad de caracteres ", resultado)
 
