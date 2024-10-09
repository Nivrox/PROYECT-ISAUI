def nombre_de_cancion(entrada):
  while True:
        verificacion_entrada = entrada[:3]
        canciones_guardadas = []
        try:
            if verificacion_entrada.lower() == "Listo":
                break
                        
            if verificacion_entrada.isalpha():
                                    cancion = entrada
                                    canciones_guardadas.append(cancion)  
            elif verificacion_entrada.isdigit(): 
                                    raise ValueError ("Ingresa solo letras")
            elif verificacion_entrada == "Listo":
                break
            else:
                if verificacion_entrada == [""]:
                
                    raise ValueError("Ingresa alguna cancion")
                    
        except ValueError:
                print ("Ingrese una cancion ")

        return cancion
def main():
      
    while True:
        try: 
            entrada = (input("Ingresa el nombre de tu cancion: "))
            print ("Pon listo cuando allas terminado")
            print (nombre_de_cancion(entrada))
        except ValueError as e:
            print (f"Error {e}")

if __name__ == main():
      
    main()