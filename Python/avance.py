#se importa la libreria tkinter para poder hacer la ventana con sus funciones 
from tkinter import* 


#se le da nombre a la ventana y se le delimita el ancho y el largo que va a tener 
vent = Tk()
vent.title("IngresoP.")
vent.geometry("500x400")
entrada1="gabriel"
#defini la funcion que permite abrir otra ventana para ingresar los productos 
def btn_ingresa():
    vent_new = Toplevel()
    vent_new.title("Ingresar P.")
    vent_new.geometry("700x550")

    entrada = StringVar()

    lbl1 =Label(vent_new,text="INGRESE LOS PRODUCTOS Y PRECIOS RESPECTIVOS")
    lbl1.config(bg="gray", fg="orange")
    lbl1.pack(padx=5, pady=5,ipadx=5, ipady=5)

    btn6 = Button(vent_new, text="SALIR", command=vent_new.destroy)
    btn6.place(x=650,y=50)
    btn6.config(bg="orange")
    #entrada de los nombres de productos 
    lbl2 =Label(vent_new,text="PRODUCTOS")
    lbl2.config(bg="gray", fg="orange")
    lbl2.place(x=40, y=60)

    entrada1 = Entry(vent_new).place(x=20, y=100)
    entrada2 = Entry(vent_new).place(x=20, y=140)
    entrada3 = Entry(vent_new).place(x=20, y=180)
    entrada4 = Entry(vent_new).place(x=20, y=220)
    entrada5 = Entry(vent_new).place(x=20, y=260)
    entrada6 = Entry(vent_new).place(x=20, y=300)
    entrada7 = Entry(vent_new).place(x=20, y=340)
    entrada8 = Entry(vent_new).place(x=20, y=380)
    entrada9 = Entry(vent_new).place(x=20, y=420)
    entrada10 = Entry(vent_new).place(x=20, y=460)
    #entrada de valores de los productos
    lbl3 =Label(vent_new,text="PRECIOS")
    lbl3.config(bg="gray", fg="orange")
    lbl3.place(x=335, y=60)
    entrada11 = Entry(vent_new).place(x=300, y=100)
    entrada12 = Entry(vent_new).place(x=300, y=140)
    entrada13 = Entry(vent_new).place(x=300, y=180)
    entrada14 = Entry(vent_new).place(x=300, y=220)
    entrada15 = Entry(vent_new).place(x=300, y=260)
    entrada16 = Entry(vent_new).place(x=300, y=300)
    entrada17 = Entry(vent_new).place(x=300, y=340)
    entrada18 = Entry(vent_new).place(x=300, y=380)
    entrada19 = Entry(vent_new).place(x=300, y=420)
    entrada20 = Entry(vent_new).place(x=300, y=460)

    btn7 = Button(vent_new, text="GUARDAR")
    btn7.place(x=320,y=500)
    btn7.config(bg="orange")

    
#esta definicion se agrego para poder cambiar el contraste de la ventana
def color():
    vent.config(bg="black")
    btn.config(fg="white")
    btn1.config(fg="white")
    btn2.config(fg="white")
    btn3.config(fg="white")
    btn4.config(fg="white")
    btn5.config(fg="white")

#ingrese una etiqueta que de indicaciones 
lbl =Label(vent,text="PRECIONE UNA OPCION")
#con config le agrege los colores a esta etiqueta y a los demas botones 
lbl.config(bg="gray", fg="orange")
lbl.pack()
#cree el primer boton que tiene la opcion de ingresar los productos y abrir una nueva ventana para los productos
btn = Button(vent, text="INGRESAR", command= btn_ingresa)
# en esta parte le indique el lugar en el que estaria
btn.place(x=0,y=30)
btn.config(bg="orange")

#este boton visualizara la lista de la que se escritibio
btn1 = Button(vent, text="VISUALIZAR")
btn1.place(x=65,y=30)
btn1.config(bg="orange")
#este es por si se han olvidado de ingresar y volverlo a ingresar 
btn2 = Button(vent, text="AÑADIR")
btn2.place(x=140,y=30)
btn2.config(bg="orange")
#en este puedo eliminar por si puse uno que no era 
btn3 = Button(vent, text="ELIMINAR")
btn3.place(x=195,y=30)
btn3.config(bg="orange")
#y lka opcion de salir que permite cerrar la ventana
btn4 = Button(vent, text="SALIR", command=vent.destroy)
btn4.place(x=260,y=30)
btn4.config(bg="orange")

#este boton me permite cambiar de contraste claro a oscuro dandole clic
btn5 = Button(vent, text="CONTRASTE",command= color)
btn5.place(x=400,y=30)
btn5.config(bg="orange")



#y esta funcion seria para que no se cierre nada y es la mas fundamental en este trabajo
vent.mainloop()
