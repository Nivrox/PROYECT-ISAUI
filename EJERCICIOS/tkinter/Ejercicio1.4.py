import tkinter
ventana = tkinter.Tk()
ventana.title("Contador tkinter")
ventana.geometry("410x100+550+300")
ventana.config(bg = "bisque2")
n = 0 

def incrementar_valor():
    valor_defect = int(casilla_1.get())
    suma = valor_defect + 1 
    casilla_1_var.set(suma)

def restar_valor():
    valor_defect = int(casilla_1.get())
    resta = valor_defect - 1
    casilla_1_var.set(resta)

def reiniciar_valor(): 
    casilla_1_var.set(0)
    
label_1 = tkinter.Label(ventana, text = "contador")
label_1.grid(row = 0, column = 0)

button_1 = tkinter.Button(text = "incrementar", command= incrementar_valor)
button_1.grid(row=0, column=10)

button_2 = tkinter.Button(text = "restar", command= restar_valor)
button_2.grid(row= 0, column = 11)

button_3 = tkinter.Button(text = "reiniciar", command= reiniciar_valor)
button_3.grid(row=0 , column = 12)

casilla_1_var = tkinter.StringVar(value=0)
casilla_1 = tkinter.Entry(ventana, textvariable=(casilla_1_var), state = "readonly", justify= "center"  )
casilla_1.grid(row = 0, column= 1)
ventana.mainloop()