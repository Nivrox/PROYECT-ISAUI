import re
contraseña = input("Ingrese una contraseña valida :  ")

if  len(contraseña) >= 8 and len(contraseña) <= 20:
    mayusculas = 0
    minusculas = 0
    caracteres_especiales = 0
    for caracter in contraseña :
        if re.search("[A-Z]", caracter):
            mayusculas += 1
        elif re.search("[a-z]",caracter):
            minusculas += 1
        elif re.search("[!@#$%/,-]" and "[1-1000]",caracter):
            caracteres_especiales += 1
    if mayusculas >= 1 and caracteres_especiales >= 1 and minusculas >= 1:
             print ("Contraseña valida!")
    else: 
        print("contraseña no valida, cumpla con las condiciones")
        print("Debe contener al menos 1 caracter en Mayuscula y 1 en minuscula")
        print("Al menos un numero o un caracter especial") 
        contraseña = input("Ingrese una contraseña valida :  ")
        if  len(contraseña) >= 8 and len(contraseña) <= 20:
            mayusculas = 0
            minusculas = 0
            caracteres_especiales = 0
            for caracter in contraseña :
                if re.search("[A-Z]", caracter):
                    mayusculas += 1
                elif re.search("[a-z]",caracter):
                 minusculas += 1
                elif re.search("[!@#$%/,-]" and "[1-1000]",caracter):
                 caracteres_especiales += 1
            if mayusculas >= 1 and caracteres_especiales >= 1 and minusculas >= 1:
                    print ("Contraseña valida!")
            else: 
                print("contraseña no valida, cumpla con las condiciones")
                print("Debe contener al menos 1 caracter en Mayuscula y 1 en minuscula")
                print("Al menos un numero o un caracter especial")     
                contraseña = input("Ingrese una contraseña valida :  ")
                if len(contraseña) >= 8 and len(contraseña) <= 20:
                    mayusculas = 0
                    minusculas = 0
                    caracteres_especiales = 0
                for caracter in contraseña :
                    if re.search("[A-Z]", caracter):
                        mayusculas += 1
                    elif re.search("[a-z]",caracter):
                        minusculas += 1
                    elif re.search("[!@#$%/,-]" and "[1-1000]",caracter):
                        caracteres_especiales += 1
                if mayusculas >= 1 and caracteres_especiales >= 1 and minusculas >= 1:
                        print ("Contraseña valida!")
                else: 
                    print("contraseña no valida, cumpla con las condiciones")
                    print("Debe contener al menos 1 caracter en Mayuscula y 1 en minuscula")
                    print("Al menos un numero o un caracter especial")     
                    contraseña = input("Ingrese una contraseña valida :  ")
        else:            
            print ("No valido debe tener min 8 caracteres")
            contraseña = input("Ingrese una contraseña valida :  ")     
            if len(contraseña) >= 8 and len(contraseña) <= 20:
                    mayusculas = 0
                    minusculas = 0
                    caracteres_especiales = 0
                    for caracter in contraseña :
                        if re.search("[A-Z]", caracter):
                            mayusculas += 1
                        elif re.search("[a-z]",caracter):
                            minusculas += 1
                        elif re.search("[!@#$%/,-]" and "[1-1000]",caracter):
                            caracteres_especiales += 1
                    if mayusculas >= 1 and caracteres_especiales >= 1 and minusculas >= 1:
                                print ("Contraseña valida!")
                    else: 
                            print("contraseña no valida, agoto sus intentos")
                            print("Debe contener al menos 1 caracter en Mayuscula y 1 en minuscula")
                            print("Al menos un numero o un caracter especial")          
            else:            
                print ("No valido debe tener min 8 caracteres, agoto sus intentos")
                contraseña = input("Ingrese una contraseña valida :  ")     
                if len(contraseña) >= 8 and len(contraseña) <= 20:
                    mayusculas = 0
                    minusculas = 0
                    caracteres_especiales = 0
                    for caracter in contraseña :
                        if re.search("[A-Z]", caracter):
                          mayusculas += 1
                        elif re.search("[a-z]",caracter):
                           minusculas += 1
                        elif re.search("[!@#$%/,-]" and "[1-1000]",caracter):
                         caracteres_especiales += 1
                    if mayusculas >= 1 and caracteres_especiales >= 1 and minusculas >= 1:
                        print ("Contraseña valida!")
                    else: 
                        print("contraseña no valida, agoto sus intentos")
                        print("Debe contener al menos 1 caracter en Mayuscula y 1 en minuscula")
                        print("Al menos un numero o un caracter especial")          
                else:            
                    print ("No valido debe tener min 8 caracteres, agoto sus intentos")
else:           
    print ("No valido debe tener min 8 caracteres")
    contraseña = input("Ingrese una contraseña valida :  ")
    if  len(contraseña) >= 8 and len(contraseña) <= 20:
            mayusculas = 0
            minusculas = 0
            caracteres_especiales = 0
            for caracter in contraseña :
                if re.search("[A-Z]", caracter):
                    mayusculas += 1
                elif re.search("[a-z]",caracter):
                 minusculas += 1
                elif re.search("[!@#$%/,-]" and "[1-1000]",caracter):
                 caracteres_especiales += 1
            if mayusculas >= 1 and caracteres_especiales >= 1 and minusculas >= 1:
                    print ("Contraseña valida!")
            else: 
                print("contraseña no valida, cumpla con las condiciones")
                print("Debe contener al menos 1 caracter en Mayuscula y 1 en minuscula")
                print("Al menos un numero o un caracter especial")     
                contraseña = input("Ingrese una contraseña valida :  ")
                if len(contraseña) >= 8 and len(contraseña) <= 20:
                    mayusculas = 0
                    minusculas = 0
                    caracteres_especiales = 0
                    for caracter in contraseña :
                        if re.search("[A-Z]", caracter):
                            mayusculas += 1
                        elif re.search("[a-z]",caracter):
                             minusculas += 1
                        elif re.search("[!@#$%/,-]" and "[1-1000]",caracter):
                            caracteres_especiales += 1
                    if mayusculas >= 1 and caracteres_especiales >= 1 and minusculas >= 1:
                            print ("Contraseña valida!")
                    else: 
                        print("contraseña no valida, agoto sus intentos")
                        print("Debe contener al menos 1 caracter en Mayuscula y 1 en minuscula")
                        print("Al menos un numero o un caracter especial")          
                else:            
                    print ("No valido debe tener min 8 caracteres, agoto sus intentos")
    else:            
        print ("No valido debe tener min 8 caracteres")

        contraseña = input("Ingrese una contraseña valida :  ")     
        if len(contraseña) >= 8 and len(contraseña) <= 20:
            mayusculas = 0
            minusculas = 0
            caracteres_especiales = 0
            for caracter in contraseña :
                if re.search("[A-Z]", caracter):
                 mayusculas += 1
                elif re.search("[a-z]",caracter):
                 minusculas += 1
                elif re.search("[!@#$%/,-]" and "[1-1000]",caracter):
                 caracteres_especiales += 1
            if mayusculas >= 1 and caracteres_especiales >= 1 and minusculas >= 1:
                    print ("Contraseña valida!")
            else: 
                print("contraseña no valida, agoto sus intentos")
                print("Debe contener al menos 1 caracter en Mayuscula y 1 en minuscula")
                print("Al menos un numero o un caracter especial")          
        else:            
            print ("No valido debe tener min 8 caracteres, agoto sus intentos")
