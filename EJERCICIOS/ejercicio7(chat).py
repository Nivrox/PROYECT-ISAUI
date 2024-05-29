import random

print("Hola, ¿cómo estás? Voy a elegir un número entre 1 y 100, tienes que adivinar.")

opcion = input("¿Estás listo? (Y/N): ")

if opcion.lower() == "y":
    numero_aleatorio = random.randint(1, 100)
    usuario = 0

    print("Perfecto, ya tengo mi número. A ver si adivinas.")
    print("Recuerda que es del 1 al 100.")

    while usuario != numero_aleatorio:
        usuario = int(input("¿Cuál crees que es mi número?: "))
        
        if usuario > numero_aleatorio:
            print("Demasiado alto.")
        elif usuario < numero_aleatorio:
            print("Demasiado bajo.")
        else:
            print("¡Correcto! ¡Has adivinado!")
else:
    print("Ok, parece que no estás listo. Estaré esperándote.")