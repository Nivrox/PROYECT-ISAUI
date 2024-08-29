import tkinter

ventana = tkinter.Tk()
ventana.geometry("300x480")

label = tkinter.Label(ventana,text=("Contador"))
label.grid(row=0,column=0)

button = tkinter.Label(ventana,text = ("+"))
button.grid(row = 1  , column = 9)

entry_var = tkinter.StringVar (value = 0)
entry = tkinter.Entry(ventana,textvariable=entry_var,state = ("readonly"), justify="center")
entry.grid(row = 0, column=2) 

button = tkinter.Label (ventana,text = ("-"))
button.grid   ( row = 1,column = 10)














ventana.mainloop()
