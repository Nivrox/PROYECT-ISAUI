monto = float(input("Ingrese el monto: "))
if monto < 0:
    print("El monto no puede ser negativo.")
    exit()

tasa = float(input("Ingrese la tasa de impuesto (en decimal, por ejemplo 0.15 para 15%): ")) 


def calcular_impuesto(monto, tasa):

    total = monto + monto * tasa
    return total

print ("El monto total con impuestos es: ", calcular_impuesto(monto, tasa))