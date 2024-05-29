import re
contraseña = input("Ingrese una contraseña valida")
mayusculas = 0
minusculas = 0
caracteresp = 0
if len(contraseña) >= 8 and len(contraseña) <= 20:
    mayusculas = 0
    minusculas = 0
    caracteresp = 0
    caracter = len(contraseña)
    while (mayusculas == 0  or minusculas == 0 or caracteresp == 0 ) and caracter < len(contraseña):
        caracter = contraseña
        if re.search("[A-Z]", caracter):
            mayusculas += 1
        elif re.search("[a-z]",caracter):
            minusculas += 1
        elif re.search("[1-1000]", caracter) and ("[!,@,#,$,%,/,-]",caracter):
            caracteresp += 1
        caracter += 1
    if mayusculas >= 1 and minusculas >= 1 and caracteresp >= 1:
        print("Contraseña valida!")
    else:
        print("contraseña no valida, cumpla con las condiciones")
        print("debe contener al menos 1 caracter en Mayuscula y 1 en minuscula")
        print("Al menos un numero o un caracter especial")
else:
    print("No valido, debe tener al menos 8 caracteres")