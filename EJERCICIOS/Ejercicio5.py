#Desarrollar un programa que convierta la temperatura farhenheit a grados celcius
#crear un medio de pregunta al usuario para que pueda convertir a la medida que le apetezca

opcion = input ("ingrese que temperatura quiere convertir entre celcius y farhenheit ")

if opcion.lower() == "celcius a farhenheit" or "celcius" : 
     celcius = float (input ("Ingrese temperatura en grados celcius "))
     farhenheit = (celcius * 9/5 ) + 32
     print ("son",farhenheit, "°" "Grados farhenheit")
elif opcion.lower() == "farhenheit a celcius" or "farhenheit":
      farhenheit = float (input ("ingrese temperatura en grados farhenheit "))
      celcius = (farhenheit - 32) * 5 / 9      
      print ("son", celcius,"°", " grados celcius")
else:
 print ("opcion no valida. Por favor, elije entre 'celcius' o 'farhenheit'")

