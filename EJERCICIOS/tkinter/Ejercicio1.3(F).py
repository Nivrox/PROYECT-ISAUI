import tkinter 

ventana = tkinter.Tk()
ventana.geometry("460x100+550+300")
ventana.title("Calculadora de factoriales")
ventana.config (bg = "bisque2")

def factorial(numero):
    resultado = 1
    for i in range (1, numero + 1 ):
        resultado *= i 
    return resultado

def Contador_numero():
    global n
    n +=1 
    Casilla_1_var.set(n)
    fact = factorial(n)
    Casilla_2_var.set(fact)
n = 1



label_1 = tkinter.Label(ventana, text="numero")
label_1.grid(row=0,column=0)


label_2 = tkinter.Label(ventana, text="Factorial (n)")
label_2.grid(row=0,column=3,)

botonsiguiente = tkinter.Button(ventana, text = "siguiente",command= Contador_numero)
botonsiguiente.grid(row=0,column=10 )

Casilla_1_var= tkinter.StringVar(value= 1)
Casilla_1_ = tkinter.Entry(ventana, textvariable=(Casilla_1_var),state="readonly", justify="center")
Casilla_1_.grid(row=0, column=1, columnspan=1, padx = 1, pady = 5 )


Casilla_2_var= tkinter.StringVar(value= factorial(n))
Casilla_2_ = tkinter.Entry(ventana, textvariable=(Casilla_2_var),state="readonly", justify="center")
Casilla_2_.grid (row=0, column=4, columnspan= 1)


ventana.mainloop()

