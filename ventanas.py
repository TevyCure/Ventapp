# Importar el modulo 
import tkinter as tk
from validacion import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
from turtle import color
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from inventariodao import inventarioBBDD

def login():
    #FUNCION PARA LO QUE HACE CUANDO SE RECIBE EL RESULTADO DE LA VALIDACION
    def llamadaValidacion(usuario,password):
        retornovalidacion=validacionLogin(usuario,password)
        a=retornovalidacion[0]
        b=retornovalidacion[1]
        if a==True and b=="jefe":
            entrarVentanaJefe()
        elif a==True and b=="vendedor":
            avisoConstruccion()
        elif a==False:
            messagebox.showerror(title = "Login incorrecto", message = "Usuario o contraseña incorrecta")
    

    #funcion para cerrar la ventana actual y abrir la funcion importada desde el archivo ventanajefe.py
    def entrarVentanaJefe():
        root.destroy()
        ventanaJefe()
    
    # Crear el objeto
    root = Tk()

    # Definir el tamaño
    root.geometry("1280x720")

    # Definir la fuente previamente habiendo importando de tkinter.font, font
    fuente=Font(
        family="Montserrat",
        size=14,
        weight="normal",
    )

    #Ingresar la función que para los entry cuando se haga click en ellos
    #se borre y se vuelva a escribir

    def haceClick(event):
        if entry.get() == 'Usuario':
            entry.delete(0,"end")
            entry.insert(0,'')
    def sacaElClick(event):
        if entry.get() =='':
            entry.insert(0,'Usuario')

    def haceClickPassword(event):
        if entry2.get() == 'Contraseña':
            entry2.delete(0,"end")
            entry2.insert(0,'')
            entry2.config(show='*')
    def sacaElClickPassword(event):
        if entry2.get() =='':
            entry2.insert(0,'Contraseña')
            entry2.config(show='')
    
    def ojo(event):
        entry2.config(show='')
    
    def ojo2(event):
        entry2.config(show='*')

    # Añadir las imagenes
    bg = PhotoImage( file = "IMG/BG.png")
    #definir el color del fondo
    root.configure(bg = "#2148c0")
    #borrar los bordes del programa
    root.overrideredirect(True)
    carrito=PhotoImage(file="IMG/CARRITO.png")
    boton=PhotoImage(file="IMG/Login btn.png")
    bordestexto=PhotoImage(file="IMG/Rectangle.png")
    botonsalir=PhotoImage(file="IMG/BOTON SALIR LOGIN.png")
    botonojo=PhotoImage(file="IMG/OJOPASSWORD 1.png")
    
    # Mostrar las imagenes usando LABEL
    label1 = Label( root, image = bg, bg='#2148c0' )
    label1.place(x = 0,y = 0)

    label1 = Label( root, image = carrito, bg='#2148c0' )
    label1.place(x = 584,y = 167)  

    botonlabel= Label(root,image=boton)
    botonsalirlabel=Label(root,image=botonsalir)
    bordestexto_label= Label(root,image=bordestexto,bg='#2148c0')
    bordestexto_label.place(x=490,y=330)
    bordestexto2_label= Label(root,image=bordestexto,bg='#2148c0')
    bordestexto2_label.place(x=490,y=400)
    #Crear cajas de textos
    #dato: se debe de definir tk (import tkinter as tk)porque usando ttk, no funciona

    #ENTRY DE USUARIO
    entry=tk.Entry(root,bg='#2148c0', font=fuente,borderwidth=0, foreground="white",insertbackground="white")
    entry.place(x=510,y=335, width=280,height=40,)
    entry.insert(0,'Usuario')
    entry.bind('<FocusIn>', haceClick)
    entry.bind('<FocusOut>', sacaElClick)

    
    #ENTRY DE PASSWORD
    entry2=tk.Entry(root,bg='#2148c0', font=fuente,borderwidth=0, foreground="white",insertbackground="white")
    entry2.place(x=510,y=405, width=280,height=40)
    entry2.insert(0,'Contraseña')
    entry2.bind('<FocusIn>', haceClickPassword)
    entry2.bind('<FocusOut>', sacaElClickPassword)

  

    def almacenar(event):
        usuario=entry.get()
        password=entry2.get()
        validacion(usuario,password)
    
    def almacenarButton():
        usuario=entry.get()
        password=entry2.get()
        llamadaValidacion(usuario,password)

    def salir():
        root.destroy()
        
    #Crear boton
    #en el boton se indica con "command" la funcion que ejecutará el boton
    button=Button(root,image=boton,borderwidth=0, command=almacenarButton,background='#2148c0')
    button.place(x=491,y=483)
    buttonsalir=Button(root,image=botonsalir,borderwidth=0,command=salir,background='#2148c0')
    buttonsalir.place(x=491,y=553)
    buttonojo=Button(root,image=botonojo,borderwidth=0,background='#2148c0')
    buttonojo.place(x=749,y=412)
    buttonojo.bind('<Button-1>',ojo)
    buttonojo.bind('<ButtonRelease-1>',ojo2)
    root.bind('<Return>',almacenar)
    # Execute tkinter
    root.mainloop()

def avisoConstruccion():
    messagebox.showerror(title = "EN CONSTRUCCION", message = "Modulo aún en construcción uwu")



# Crear la funcion para la ventana del Jefe de Ventas
def ventanaJefe():
    root = Tk()
    # Definir el tamaño
    root.geometry("1280x720")
    # Definir la fuente previamente habiendo importando de tkinter.font, font
    fuente=Font(
        family="Montserrat",
        size=14,
        weight="normal",
    )
    #FUNCIONES DE LOS BOTONES, SE LLAMAN CON "COMMAND"
    def abrirVentanaReportes():
        root.destroy()
        ventanaReportes()
    
    def abrirVentanaInventario():
        root.destroy()
        ventanaInventario()
    
    
    def cerrarSesion():
        root.destroy()
        login()
    # Añadir las imagenes
    bg = PhotoImage( file = "IMG/BG.png")
    root.configure(bg = "#2148c0")
    #quitar los bordes del programa
    root.overrideredirect(True)
    botoninventario=PhotoImage(file="IMG/BOTON INVENTARIO.png")
    botonreportes=PhotoImage(file="IMG/BOTON REPORTESSINFONDO.png")
    botoniniciarcerrar=PhotoImage(file="IMG/BOTON INICIARCERRAR DIA.png")
    botonvendedor=PhotoImage(file="IMG/BOTON VENDEDOR.PNG")
    botoncerrarsesion=PhotoImage(file="IMG/BOTON CERRAR SESION.PNG")
  
    # Mostrar las imagenes usando LABEL
    label1 = Label( root, image = bg, bg='#2148c0' )
    label1.place(x = 0,y = 0)

    botonlabel= Label(root,image=botoninventario)
    botonlabel2= Label(root,image=botonreportes)
    botonlabel3= Label(root, image=botoniniciarcerrar)
    botonlabel4= Label(root, image=botonvendedor)
    botonlabel5= Label(root, image=botoncerrarsesion)

    #Crear boton y asignar función correspondiente con "command"
    button=Button(root,image=botoninventario,borderwidth=0,bg='#2148c0', command=abrirVentanaInventario)
    button.place(x=155.31,y=145.32)

    button2=Button(root,image=botonreportes,borderwidth=0,bg='#2148c0', command=avisoConstruccion)
    button2.place(x=705,y=145)

    button3=Button(root,image=botoniniciarcerrar,borderwidth=0,bg='#2148c0', command=avisoConstruccion)
    button3.place(x=152.31,y=405.32)

    button4=Button(root,image=botonvendedor,borderwidth=0,bg='#2148c0', command=avisoConstruccion)
    button4.place(x=705,y=405.32)
    
    button5=Button(root,image=botoncerrarsesion,borderwidth=0,bg='#264ECA', command=cerrarSesion)
    button5.place(x=881,y=34)

    # Execute tkinter
    root.mainloop()

def ventanaInventario():
    
    def salirInventario():
        root.destroy()
        ventanaJefe()

    root = Tk()

    root.geometry("1280x720")
    root.configure(bg = "#2148C0")
    root.overrideredirect(True)
    style = ttk.Style()
    style.theme_use('alt')
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Montserrat', 11)) # Modify the font of the body
    style.configure("mystyle.Treeview.Heading",background="white", font=('Montserrat',13,'bold'),foreground="#244bc5") # Modify the font of the headings
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

    canvas = Canvas(
        root,
        bg = "#2148C0",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file="IMG/image_1.png")
    image_1 = canvas.create_image(
        541.0,
        541.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file="IMG/button_1.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=salirInventario,
        relief="flat",bg='#2148c0'
    )
    button_1.place(
        x=905.0,
        y=73.0,
        width=228.0,
        height=90.0
    )

    button_image_2 = PhotoImage(
        file="IMG/button_2.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=avisoConstruccion,
        relief="flat",bg='#2148c0'
    )
    button_2.place(
        x=656.3004760742188,
        y=73.0,
        width=222.6995391845703,
        height=90.0
    )

    button_image_3 = PhotoImage(
        file="IMG/button_3.png")
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=avisoConstruccion,
        relief="flat",bg='#2148c0'
    )
    button_3.place(
        x=149.0,
        y=76.0,
        width=226.0,
        height=90.0
    )

    button_image_4 = PhotoImage(
        file="IMG/button_4.png")
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=avisoConstruccion,
        relief="flat",bg='#2148c0'
    )
    button_4.place(
        x=401.0,
        y=76.0,
        width=226.0,
        height=90.0,
    )

    tv = ttk.Treeview(root,columns=(1,2,3,4),show="headings",style="mystyle.Treeview")
    tv.pack()
    tv.place(
        x=149.0,
        y=176.0,
        width=982,
        height=500
    )


    tv.heading(1, text="CODIGO(SKU)")
    tv.heading(2,text="DESCRIPCION")
    tv.heading(3,text="VALOR NETO")
    tv.heading(4,text="CATEGORIA")
    
    tv.column(1, anchor=CENTER, width=60)
    tv.column(2,anchor=CENTER, width=60)
    tv.column(3,anchor=CENTER, width=60)
    tv.column(4,anchor=CENTER, width=60)

    #recibir elementos de la base de datos y guardarlos en una lista
    elementos=inventarioBBDD()
    count=0
    for elemento in elementos:
        tv.insert(parent='', index='end',iid=count, text="",values=(elemento[0],elemento[1],elemento[2],elemento[3]))
        count+=1
    print(elementos)
    root.resizable(False, False)
    root.mainloop()


def ventanaReportes():
    root = Tk()
    # Definir el tamaño
    root.geometry("1280x720")
    # Definir la fuente previamente habiendo importando de tkinter.font, font
    fuente=Font(
        family="Montserrat",
        size=14,
        weight="normal",
    )
    # Añadir las imagenes
    bg = PhotoImage( file = "IMG/BG.png")
    root.configure(bg = "#2148c0")
    root.overrideredirect(True)

    #AGREGAR LOS BOTONES PARA LA VENTANA REPORTES
    
  
    # Mostrar las imagenes usando LABEL
    label1 = Label( root, image = bg, bg='#2148c0' )
    label1.place(x = 0,y = 0)

    #AGREGAR LOS LABEL

    #CREAR BOTONES
   

    

    # Execute tkinter
    root.mainloop()

