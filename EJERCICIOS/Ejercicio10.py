# Crea un juego de ahorcado donde el jugador debe adivinar una palabra oculta 
# Antes de que se agoten los intentos. Puedes hacerlo con una lista predefinida de palabra

import random

print("Vamos a jugar al ahorcado...")
print("Yo voy a elegir una palabra, tú tendrás que adivinarla.")
respuesta_usuario = input("¿Estás listo? (si/mandale/yes): ")

if respuesta_usuario.lower() in ["si", "mandale", "yes"]:
    palabras = ["paracaidas", "escuela", "avioneta"]
    palabra_aleatoria = random.choice(palabras)
    vida = 6
    caracter_correcto = ["_"] * len(palabra_aleatoria)  # Inicializa con "_" para cada letra de la palabra
    caracter_incorrecto = [] #guarda los caracteres incorrectos que ingresa el usuario mediante letra

    print("Decime qué palabra elegí, tenés 6 oportunidades")

    while vida > 0:
        print("Vidas restantes:", vida)
        print("Palabra:", " ".join(caracter_correcto))  # Muestra la palabra con letras adivinadas y "_"
       #"".join ordena los datos dentro de caracter correcto en una cadena de caracteres  

        letra = input("Dime una letra: ").lower()
       

        if letra in palabra_aleatoria:
            print("¡Correcto!")
            # Actualiza caracter_correcto con la letra adivinada en las posiciones correctas
            for i in range(len(palabra_aleatoria)):
                if palabra_aleatoria[i] == letra:
                    caracter_correcto[i] = letra #caracater_correcto se actualiza en cada posicion que este esa letra
                if palabra_aleatoria == letra: #Si cada caracter dentro de letra es igual a la palabra aleatoria 
                   caracter_correcto[i] = letra #caracater_correcto se actualiza en cada posicion que este esa letra   

            if "_" not in caracter_correcto:  # Si ya se adivinaron todas las letras
                print("¡Ganaste! La palabra era:", palabra_aleatoria)

                break 
        else:
            print("Incorrecto.")
            vida -= 1
            caracter_incorrecto.append(letra)
            print("Incorrectos hasta ahora:", caracter_incorrecto)

    if vida == 0:
        print("¡Oh no! Te has quedado sin vidas. La palabra era:", palabra_aleatoria)

    
        


