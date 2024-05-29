#Desarrolla un programa en Python que convierta una cantidad de dinero de dólares estadounidenses a euros
#El programa debe solicitar al usuario que ingrese la cantidad en dólares y luego mostrar la cantidad equivalente en euros
# utilizando un tipo de cambio fijo.  



tipodecambio = input ("Ingrese el tipo de cambio ")


if tipodecambio.lower() == "dolar a euro" or "dolar":
   dolares = float (input ("ingrese la cantidad de dolares"))
   euros = (0.94 * dolares)
   print ("la cantidad de dolares en euro es de ", euros)
elif tipodecambio.lower == "euros":
    euros = float (input ("ingrese la cantidad de euros"))
    dolares = (1.07 * euros )
    print ("La cantidad de euros en dolares es de ", dolares)
else:
   print ("opcion no valida. Por favor, elija entre 'dolar' o 'euro'")

 

