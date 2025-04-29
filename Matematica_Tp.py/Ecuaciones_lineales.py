import numpy as np

def ingresar_sistema():
    # Pedimos al usuario el número de incógnitas (tamaño de la matriz)
    n = int(input("Ingrese el número de incógnitas del sistema: "))

    # Inicializamos la matriz de coeficientes y el vector de términos independientes
    matriz_coeficientes = []
    vector_terminos_independientes = []

    # Solicitamos los coeficientes del sistema al usuario
    print("Ingrese los coeficientes de cada ecuación (uno por uno):")
    for i in range(n):
        ecuacion = []
        for j in range(n):
            coef = float(input(f"Coeficiente de la variable x{j+1} en la ecuación {i+1}: "))
            ecuacion.append(coef)
        matriz_coeficientes.append(ecuacion)
        termino_independiente = float(input(f"Término independiente de la ecuación {i+1}: "))
        vector_terminos_independientes.append(termino_independiente)

    # Convertimos las listas a arrays de numpy
    A = np.array(matriz_coeficientes)
    b = np.array(vector_terminos_independientes)

    return A, b

def mostrar_matriz_y_determinante(A):
    print("\nMatriz de coeficientes:")
    print(A)

    # Calculamos el determinante de la matriz de coeficientes
    determinante = np.linalg.det(A)
    print(f"\nDeterminante de la matriz: {determinante}")

    return determinante

def resolver_sistema(A, b, determinante):
    # Verificamos si el sistema es determinado o indeterminado
    if determinante != 0:
        print("\nEl sistema es determinado. Tiene una solución única.")
        # Resolvemos el sistema
        soluciones = np.linalg.solve(A, b)
        print("\nSoluciones:")
        for i, sol in enumerate(soluciones):
            print(f"x{i+1} = {sol}")
    else:
        print("\nEl sistema es indeterminado no tiene solución.")

# Programa principal
A, b = ingresar_sistema()
determinante = mostrar_matriz_y_determinante(A)
resolver_sistema(A, b, determinante)
