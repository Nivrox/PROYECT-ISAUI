#Desarrolla un juego en el que el programa selecciona aleatoriamente un numero
#Entre el 1 y 100 el jugador debve adivinarlo. el programa debe proporcionar pistas
#si el numero ingresado es demasiado alto o demasiado bajo
#el juego debe continuar hasta que el jugador adivine
import random

print ("Hola como estas voy a elegir un numero entre el 1 y el 100 tienes que adivinar")

opcion = input ("¿Estas listo? Y/N:  ")

if opcion.lower() == "y" :

    numero_aleatorio = random.randint(1, 100)
    usuario = 0 
    
    print ("perfecto!, ya tengo mi numero a ver si adivinas...")

    while usuario != numero_aleatorio:

        usuario = int(input("¿Cual crees que es?: "))
          #Comprueba si el numero ingresado es mayor al numero aleatorio 
        
        if usuario < numero_aleatorio:  
            if usuario <= 0:
                 print ("No, Recuerda que el numero es del 1 - 100 ")
            else: 
               print ("Demasiado bajo") 
        elif usuario > numero_aleatorio:
            if usuario >= 101 :  
                print ("No, Recuerda que el numero es del 1 - 100 ")
            else:    
                print("Demasiado alto")
        else:
         print ("Bien, adivinaste!")

else:
     programa = print ("Ok... Parece que no estas listo, estare esperandote....")
                  
