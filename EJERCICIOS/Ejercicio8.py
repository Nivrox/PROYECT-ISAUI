#Escribe un programa que genere una contraseña aleatoria para el usuraio
#La contraseña debe tener una combinacion de letras y caracteres especiales-
#El programa debe mostrar la contraseña al usuario
import random
import string 
usuario = input ("Hola!, ¿estas buscando una contraseña? Y/N: ")

if usuario.lower() == "y" or "si":

    print ("Deja que genere una por vos:")

    caracteres_especiales = "#,$,%,/,!,?,*,+"
    mayusculas = "A-Z"
    numeros = "1 - 10"
    n = 3
    p = 4
    k = 2
    minusculas = random.sample ( string.ascii_lowercase, k)
    mayusculas = random.sample ( mayusculas, n)
    caracteres_especiales = random.sample ( caracteres_especiales, n)
    numeroscaract = random.sample (numeros, p)
    contraseña_aleatoria = ''.join(caracteres_especiales + mayusculas + minusculas + numeroscaract)
    print ("esta es tu contraseña: ", contraseña_aleatoria)
else:
    print ("Bueno curtite")
                  
       



    