def sacar_promedios (n):
    sum = 0 
    promedio = 0
    promedios = {
        "juan" : [10,3,6,7],
        "julian": [2,6,3,7],
        "mateo" : [5,10,3,6],
        "sofi" : [3,3,10,10],
    }
    if n  == "juan":
        for numero in promedios["juan"]:
            sum += numero
            promedio = sum / len("juan")
           
    if n  == "julian":
        for numero in promedios["julian"]:
            sum += numero
            promedio = sum / len("julian")
            
    if n == "mateo":
        for numero in promedios ["mateo"]:
            sum += numero
            promedio = sum / len("mateo")
            
    if n == "sofi":
        for numero in promedios ["sofi"]:

            sum += numero
            promedio = sum / len("sofi")
    print ("este es su promedio: ",promedio)

    return promedio
usuario = input ("Ingresa el nombre de la persona : ")
while True:
    try:

        if usuario.lower() == "julian" and "sofi" and "mateo" and "juan": 
            print (sacar_promedios(usuario))
            break
    except ValueError:
        print ("dato no valido")