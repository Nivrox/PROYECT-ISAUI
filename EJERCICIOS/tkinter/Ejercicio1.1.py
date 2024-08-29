import tkinter 

ventana = tkinter.Tk()
ventana.geometry("300x100")
ventana.title("Contador")
ventana.config(bg = "red")


def aumentar(): 
    suma= int(Casilla_1_.get())
    nuevo_valor= suma +1
    Casilla_1_var.set(nuevo_valor)


label_1 = tkinter.Label(ventana, text="Contador")
label_1.grid(row=0,column=0)
button_1 = tkinter.Button(ventana, text = "+",command=aumentar)
button_1.grid(row=1,column=1,columnspan=3, padx=5,pady=5)

Casilla_1_var= tkinter.StringVar(value=0)
Casilla_1_ = tkinter.Entry(ventana, textvariable=(Casilla_1_var),state="readonly", justify="center")
Casilla_1_.grid(row=0, column=1, columnspan=2, )
ventana.mainloop()