import tkinter as tk
def abrir_dashboard():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Panel de Control")
    root.geometry("800x500")

    # Frame lateral (parte izquierda)
    frame_lateral = tk.Frame(root, bg="lightgray", width=200)
    frame_lateral.pack(side="left", fill="y")

    # Sección del perfil del usuario (dentro del frame lateral)
    frame_perfil = tk.Frame(frame_lateral, bg="lightblue", height=100)
    frame_perfil.pack(fill="x")

    # Nombre del usuario y rol
    nombre_perfil = tk.Label(frame_perfil, text="DIRECTOR", font=("Arial", 14, "bold"), bg="lightblue")
    nombre_perfil.pack(pady=10)

    rol_perfil = tk.Label(frame_perfil, text="Admin", font=("Arial", 10), bg="lightblue")
    rol_perfil.pack()

    # Opciones del menú lateral
    items_menu = [("Socios", "👥"), ("Préstamos", "📚"), ("Libros", "📖")]

    for item, icono in items_menu:
        btn = tk.Button(frame_lateral, text=f"{icono} {item}", font=("Arial", 12), bg="lightgray", bd=0, anchor="w")
        btn.pack(fill="x", pady=5, padx=10)

    # Frame principal (parte derecha)
    frame_principal = tk.Frame(root, bg="white")
    frame_principal.pack(side="right", fill="both", expand=True)

    # Texto en el área principal
    label_bienvenida = tk.Label(frame_principal, text="Bienvenido", font=("Arial", 18), bg="white")
    label_bienvenida.pack(pady=20)

    # Iniciar la aplicación
    root.mainloop()