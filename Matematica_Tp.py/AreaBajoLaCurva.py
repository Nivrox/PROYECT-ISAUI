def calcular_GJ(coeficientes):
    def gauss_jordan(matriz):
        filas = len(matriz)
        columnas = len(matriz[0])
        
        for i in range(filas):
            if matriz[i][i] == 0:
                for k in range(i + 1, filas):
                    if matriz[k][i] != 0:
                        matriz[i], matriz[k] = matriz[k], matriz[i]
                        break
                else:
                    continue

            pivote = matriz[i][i]
            for j in range(i, columnas):
                matriz[i][j] /= pivote

            for k in range(filas):
                if k != i:
                    factor = matriz[k][i]
                    for j in range(i, columnas):
                        matriz[k][j] -= factor * matriz[i][j]

        return matriz

    def determinar_tipo_sistema(matriz):
        filas = len(matriz)
        columnas = len(matriz[0])
        es_indeterminado = False

        for i in range(filas):
            if all(matriz[i][j] == 0 for j in range(columnas - 1)) and matriz[i][-1] != 0:
                return "Incompatible"
            if all(matriz[i][j] == 0 for j in range(columnas - 1)) and matriz[i][-1] == 0:
                es_indeterminado = True
                break

        return "Compatible Indeterminado" if es_indeterminado else "Compatible Determinado"

    try:
        matriz = [list(map(float, coef.split())) for coef in coeficientes]
        if any(len(fila) != 4 for fila in matriz):
            raise ValueError("Cada fila debe contener exactamente 4 valores.")
    except ValueError as e:
        messagebox.showerror("Error de entrada", str(e))
        return None, "Error de entrada"

    matriz_resuelta = gauss_jordan(matriz)
    tipo_sistema = determinar_tipo_sistema(matriz_resuelta)
    return matriz_resuelta, tipo_sistema

def mostrar_resultados():
    coeficientes = [entry1.get(), entry2.get(), entry3.get()]
    matriz_resuelta, tipo_sistema = calcular_GJ(coeficientes)
    
    resultado_texto = ""
    if matriz_resuelta is not None:
        resultado_texto += "Matriz resultante:\n"
        max_len = max(len(f"{num:.2f}".rstrip('0').rstrip('.') if num % 1 != 0 else f"{int(num)}") for fila in matriz_resuelta for num in fila)
        for i, fila in enumerate(matriz_resuelta):
            fila_texto = " ".join(f"{num:.2f}".rstrip('0').rstrip('.').rjust(max_len) if num % 1 != 0 else f"{int(num)}".rjust(max_len) for num in fila[:-1]) + " | " + (f"{fila[-1]:.2f}".rstrip('0').rstrip('.').rjust(max_len) if fila[-1] % 1 != 0 else f"{int(fila[-1])}".rjust(max_len))
            if i == 0:  # Primera fila
                resultado_texto += f"╔ {fila_texto} ╗\n"
            elif i == len(matriz_resuelta) - 1:  # Última fila
                resultado_texto += f"╚ {fila_texto} ╝\n"
            else:  # Filas del medio
                resultado_texto += f"║ {fila_texto} ║\n"
        resultado_texto += f"\nTipo de sistema: {tipo_sistema}"

        if tipo_sistema == "Compatible Indeterminado":
            resultado_texto += "\nEl sistema tiene infinitas soluciones."
    else:
        resultado_texto = "El sistema es Incompatible. No tiene soluciones."
    
    resultado_text.config(state=tk.NORMAL)
    resultado_text.delete(1.0, tk.END)
    resultado_text.insert(tk.END, resultado_texto)
    resultado_text.config(state=tk.DISABLED)

def borrar_campos():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    resultado_text.config(state=tk.NORMAL)
    resultado_text.delete(1.0, tk.END)
    resultado_text.config(state=tk.DISABLED)

def validar_entrada(texto):
    if texto == "":
        return True
    if texto[0] == " ":
        return False
    if "  " in texto:
        return False
    if texto.count(" ") > 3:
        return False
    if not all(c.isdigit() or c.isspace() or c == '.' or c == '-' for c in texto):
        return False
    return True

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Método de Gauss-Jordan")
ventana.geometry("650x535")
ventana.configure(bg="#8f7456")    
ventana.resizable(False,False)

marco = tk.LabelFrame(ventana, text="Calcular Gauss-Jordan", bg="#bdb19d", font=('Times New Roman', 12, 'bold'))
marco.place(x=25, y=25, width=600, height=485)  

validate_command = marco.register(validar_entrada)

# Crear los widgets
tk.Label(marco, text="Ingrese los coeficientes y el valor de igualdad de la ecuación 1 (x1 y1 z1 i1):", bg="#bdb19d", font=('Times New Roman', 12)).pack()
entry1 = tk.Entry(marco, validate="key", validatecommand=(validate_command, '%P'))
entry1.pack()

tk.Label(marco, text="Ingrese los coeficientes y el valor de igualdad de la ecuación 2 (x2 y2 z2 i2):", bg="#bdb19d", font=('Times New Roman', 12)).pack()
entry2 = tk.Entry(marco, validate="key", validatecommand=(validate_command, '%P'))
entry2.pack()

tk.Label(marco, text="Ingrese los coeficientes y el valor de igualdad de la ecuación 3 (x3 y3 z3 i3):", bg="#bdb19d", font=('Times New Roman', 12)).pack()
entry3 = tk.Entry(marco, validate="key", validatecommand=(validate_command, '%P'))
entry3.pack()

tk.Label(marco, text="En caso de no contar con 'x', 'y' o 'z' en su ecuacion, reemplazar por 0", bg="#bdb19d", font=('Times New Roman', 12)).pack()    

boton_calcular = tk.Button(marco, text="Calcular", command=mostrar_resultados, borderwidth=2, height=1, width=10, anchor="center", bg="#afbad2", font=('Times New Roman', 10, 'bold'))
boton_calcular.place(x=155, y=170)

boton_borrar = tk.Button(marco, text="Borrar", command=borrar_campos, borderwidth=2, height=1, width=10, anchor="center", bg="#afbad2", font=('Times New Roman', 10, 'bold'))
boton_borrar.place(x=255, y=170)

boton_volver = tk.Button(marco, text="Volver", command=marco.quit, borderwidth=2, height=1, width=10, anchor="center", bg="#afbad2", font=('Times New Roman', 10, 'bold'))
boton_volver.place(x=355, y=170)

resultado_text = tk.Text(marco, height=10, width=50, font=('Times New Roman', 12, 'bold'))
resultado_text.place(x=50, y=220, width=500, height=200)
resultado_text.config(state=tk.DISABLED)

# Iniciar el bucle principal de la interfaz gráfica
