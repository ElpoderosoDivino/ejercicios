#se importa la libreria tkinter para poder hacer la ventana con sus funciones 
from tkinter import* 
#se le da nombre a la ventana y se le delimita el ancho y el largo que va a tener 
vent = Tk()
vent.title("IngresoP.")
vent.geometry("1000x700")
entrada1="gabriel"
#defini la funcion que permite ingresar los datos de productos y precios 
def btn_ingresa():
    lbl1 =Label(vent,text="INGRESE LOS PRODUCTOS Y PRECIOS RESPECTIVOS")
    lbl1.config(bg="black", fg="orange")
    lbl1.place(x=350,y=60)
    #entrada de los productos 
    lbl2 =Label(vent,text="PRODUCTOS")
    lbl2.config(bg="black", fg="orange")
    lbl2.place(x=40, y=90)
    
    entrada1 = Entry(vent).place(x=20, y=130),Entry(vent).place(x=20, y=170), Entry(vent).place(x=20, y=210), Entry(vent).place(x=20, y=250), 
    Entry(vent).place(x=20, y=290), Entry(vent).place(x=20, y=330), Entry(vent).place(x=20, y=370), Entry(vent).place(x=20, y=410), Entry(vent).place(x=20, y=450),
    Entry(vent).place(x=20, y=490)

    #entrada de valores 
    lbl3 =Label(vent,text="PRECIOS")
    lbl3.config(bg="black", fg="orange")
    lbl3.place(x=335, y=90)
    
    entrada2 = Entry(vent).place(x=300, y=130),  Entry(vent).place(x=300, y=170), Entry(vent).place(x=300, y=210), Entry(vent).place(x=300, y=250),
    Entry(vent).place(x=300, y=290), Entry(vent).place(x=300, y=330), Entry(vent).place(x=300, y=370), Entry(vent).place(x=300, y=410), Entry(vent).place(x=300, y=450),
    Entry(vent).place(x=300, y=490)
#la opcion añadir lo que hace es que añade mas espacios para mas productos y precions
def btn_añadir():
    lbl4 =Label(vent,text="PRODUCTOS")
    lbl4.config(bg="black", fg="orange")
    lbl4.place(x=540, y=90)

    entrada1 = Entry(vent).place(x=513, y=130),Entry(vent).place(x=513, y=170), Entry(vent).place(x=513, y=210), Entry(vent).place(x=513, y=250), 
    Entry(vent).place(x=513, y=290), Entry(vent).place(x=513, y=330), Entry(vent).place(x=513, y=370), Entry(vent).place(x=513, y=410), Entry(vent).place(x=513, y=450),
    Entry(vent).place(x=513, y=490)

    lbl5 =Label(vent,text="PRECIOS")
    lbl5.config(bg="black", fg="orange")
    lbl5.place(x=835, y=90)
    
    entrada2 = Entry(vent).place(x=800, y=130),  Entry(vent).place(x=800, y=170), Entry(vent).place(x=800, y=210), Entry(vent).place(x=800, y=250),
    Entry(vent).place(x=800, y=290), Entry(vent).place(x=800, y=330), Entry(vent).place(x=800, y=370), Entry(vent).place(x=800, y=410), Entry(vent).place(x=800, y=450),
    Entry(vent).place(x=800, y=490)
#esta definicion se agrego para poder cambiar el contraste de la ventana, etiquetas y botones
def color():
    vent.config(bg="gray")
    btn.config(fg="white")
    btn1.config(fg="white")
    btn2.config(fg="white")
    btn3.config(fg="white")
    btn4.config(fg="white")
    lbl.config(bg="black")
#ingrese una etiqueta que de indicaciones 
lbl =Label(vent,text="PRECIONE UNA OPCION")
lbl.config(bg="gray", fg="orange")
lbl.pack()
#permite ingresar los datos 
btn = Button(vent, text="INGRESAR", command= btn_ingresa)
btn.place(x=0,y=30)
btn.config(bg="orange")
#esta variable es para poder dar opciones al usuario de que desea eliminar 
opcion = IntVar()
#se define para la elleccion del usuario
def comOk():
    op = opcion.get()
    if op == 1:
        python.set(0)
        php.set(0)
        ruby.set(0)
        c.set(0)
        cc.set(0)
    elif op == 2:
        listLenguajes.delete(0,END)
    elif op == 3:
        python.set(0)
        php.set(0)
        ruby.set(0)
        c.set(0)
        cc.set(0)
        listLenguajes.delete(0,END)
#se define para posicionar las opciones y para cumplir la opcion deseada por el usuario
def reset():
    radioSel1 = Radiobutton(vent, text="Reiniciar lenguajes", variable = opcion, value = 1)
    radioSel1.place(x=400,y=580)

    radioSel2 = Radiobutton(vent, text="Reiniciar lista", variable = opcion, value = 2)
    radioSel2.place(x=400,y=600)

    radioSel3 = Radiobutton(vent, text="Reiniciar todo", variable = opcion, value = 3)
    radioSel3.place(x=400,y=620)   

    botonOk = Button(vent, text="OK", command  =comOk)
    botonOk.place(x=400,y=640)
#sirve para poder ingresar mas datos si no han sido sufie¡cientes 
btn1 = Button(vent, text="AÑADIR", command=btn_añadir)
btn1.place(x=65,y=30)
btn1.config(bg="orange")
#da opciones al usuario para ver que desea eliminar 
btn2 = Button(vent, text="ELIMINAR", command=reset)
btn2.place(x=119,y=30)
btn2.config(bg="orange")
#salir de la ventana 
btn3 = Button(vent, text="SALIR", command=vent.destroy)
btn3.place(x=183,y=30)
btn3.config(bg="orange")
#se cambia el contraste a oscuro 
btn4 = Button(vent, text="CONTRASTE",command= color)
btn4.place(x=900,y=30)
btn4.config(bg="orange")
#esta funcion seria para que no se cierre nada y es la mas fundamental en este trabajo
vent.mainloop()