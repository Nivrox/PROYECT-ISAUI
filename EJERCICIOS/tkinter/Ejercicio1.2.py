import tkinter 

ventana = tkinter.Tk()
ventana.geometry("300x100+550+300")
ventana.title("Contador")
ventana.config(bg = "bisque2")


def aumentar(): 
    valor_defect = int(Casilla_1_.get())
    nuevo_valor = valor_defect- 1
    Casilla_1_var.set(nuevo_valor)


label_1 = tkinter.Label(ventana, text="Contador")
label_1.grid(row=0,column=0)
button_1 = tkinter.Button(ventana, text = "-",command=aumentar)
button_1.grid(row=0,column=5,columnspan=4, padx= 5,pady= 5)

Casilla_1_var= tkinter.StringVar(value= 88)
Casilla_1_ = tkinter.Entry(ventana, textvariable=(Casilla_1_var),state="readonly", justify="center")
Casilla_1_.grid(row=0, column=1, columnspan=2, padx = 10, pady = 5  )
ventana.mainloop()