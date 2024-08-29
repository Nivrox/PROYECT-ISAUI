
#Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el
#valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el
#máximo y el mínimo, utilizando la función anterior.
def calcularmax_y_min(lista):
    # Aseguramos que la lista no esté vacía
    if not lista:
        print("La lista está vacía.")
        return None, None
    
    # Inicializamos los valores de max y min con el primer elemento de la lista
    numeromax = lista[0]
    numeromin = lista[0]
    
    for numero in lista:
        if numero > numeromax:
            numeromax = numero
        if numero < numeromin:
            numeromin = numero
    
    print("Este es tu número mínimo:", numeromin, "Este es tu número máximo:", numeromax)
    return numeromax, numeromin

 # Solicita al usuario que ingrese los números separados por comas
entrada = input("Ingrese los números enteros separados por comas: ")

# Divide la cadena de entrada en una lista de cadenas usando la coma como separador
numeros_str = entrada.split(',')

# Convierte cada cadena en un entero y almacénalo en una nueva lista
numeros = [int(numero) for numero in numeros_str]

resultado = calcularmax_y_min(numeros)