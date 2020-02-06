from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import ImageTk, Image 
import os

import cv2

from tkinter import filedialog

import socket
from urllib.request import urlopen



loginWindow=Tk()
mainMenu=Tk()


def imprimir(texto):
     print (texto)

def mostrar(ventana):
     return ventana.deiconify # Muestra una ventana

def ocultar(ventana):
     return ventana.withdraw() # Oculta una ventana

def ejecutar(f): 
    loginWindow.after(100, f)


def cerrar_splashscreen():
    ejecutar(ocultar(splashScreen))
    ejecutar(mostrar(loginWindow))


def progress(currentValue): #Llama
    progressbar["value"]=currentValue


#Funcion ventana añadir nuevo usuario
def registroUsuario(username, contra):
    usuario_info = username
    contra_info = contra
    file = open("usuario_info.txt", "a")
    file.write(usuario_info + "\n")
    file.write(contra_info + "\n")
    file.close()
    messagebox.showinfo("Listo","Quedaste registrado")


def hayInternet(): #Comprueba que exista alguna conexion a internet.
   try:
        response = urlopen('https://www.google.com/', timeout=10)
        return True
   except: 
        return False

#Funciones de la ventana principal (Pestaña principal)

def verificarUsuario(username, contra):
    
    usuario_info = username
    contra_info = contra

    if usuario_info == '' or contra_info == '':
        messagebox.showwarning("Cuidado", "Revisa tus datos bro")
        
    else:
        print(usuario_info, contra_info)
        lista_archivos = os.listdir()
      
        archivo = open("Python/Archivos/usuario_info.txt", "r")
        verificar = archivo.read().splitlines()
        print(verificar)
        if usuario_info in verificar:
            posicion = verificar.index(usuario_info)
            print (usuario_info)
            print(posicion)
            print(contra_info)
            if contra in verificar[posicion+1]:
                messagebox.showinfo("Listo", "Ya quedo bro")
                loginWindow.destroy() #Cierra el login
                abrirVentanaMenuPrincipal() #Manda a llamar a la siguiente funcion para abrir la ventana principal.
            else:
                messagebox.showwarning("Cuidado", "Password incorrecto")
        else:
            messagebox.showwarning("Cuidado", "Usuario incorrecto")
         
def llenarInicio(ruta):
    if ruta == '':
        messagebox.showwarning("Cuidado", "no seleccionaste nada bro :( ")
    else:
        archivo = open(ruta, "r")
        datos = archivo.read().splitlines()

        #Primera linea: Nombre
        posicion = datos.index("Nombre:")
        nombre = datos[posicion+1] 

        #Primera linea: Diametro
        posicion = datos.index("Diametro:")
        diametro = datos[posicion+1] 

        #Segunda linea: Espesor
        posicion = datos.index("Espesor:")
        espesor = datos[posicion+1]

        #Segunda linea: Espesor
        posicion = datos.index("Largo:")
        largo = datos[posicion+1]

        print(diametro, espesor, largo)

        TxtNombre.insert(0,nombre)
        TxtDiametro.insert(0,diametro)
        TxtEspesor.insert(0,espesor)
        TxtLargo.insert(0,largo) 
    
def abrirArchivo():
    ruta=filedialog.askopenfilename(initialdir="/Proyecto de Titulacion (Python)/Python/Archivos", title ="Seleccione archivo", filetypes=(("txt files", "*.txt"), ("all files","*.*")))
    print(ruta)
    llenarInicio(ruta)

def guardarArchivo():

    if TxtNombre.get() == '' or TxtDiametro.get() == '' or TxtEspesor.get() == '' or TxtLargo.get() == '':
        messagebox.showwarning("Cuidado","Revisa tus datos bro")
    else:
        lista_archivos = os.listdir()
        if TxtNombre.get() + ".txt" in lista_archivos:
            messagebox.showwarning("Cuidado", "Ese ya esta guardado bro")
        else:
            archivoNuevo = open(TxtNombre.get() + ".txt","w")
            archivoNuevo.write("Nombre:" + "\n")
            archivoNuevo.write(TxtNombre.get() + "\n")
            archivoNuevo.write("Diametro:" + "\n")
            archivoNuevo.write(TxtDiametro.get() + "\n")
            archivoNuevo.write("Espesor:" + "\n")
            archivoNuevo.write(TxtEspesor.get() + "\n")
            archivoNuevo.write("Largo:" + "\n")
            archivoNuevo.write(TxtLargo.get())
            archivoNuevo.close()
            messagebox.showinfo("Ya quedo", "Ya se guardo puñetas")



#Funciones de la ventana calibrar
def obtenerRadioButton(Avance, direccion):
    '''
    Obtiene el avance y la direccion (el motor que se movera) y extrae el valor del radio button
    despues de esto llama a la funcion de moverMotor y le pasa los 3 parametros.
    '''
    unidades = unidadMedida.get()
    if unidades == 1:
        print("Centimetros")
        #moverMotor("Centimetros",Avance, direccion)
    elif unidades == 2:
        print("Pulgadas")
        #moverMotor("Pulgadas",Avance, direccion)
    else:
        print("An option must be selected")

def video_loop():
    '''
    This function works in the case that if necessary active a camera or improve the project.
    '''
    ok, frame = cap.read()  # read frame from video stream
    if ok:  # frame captured without any errors
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # convert colors from BGR to RGBA
        cv2.circle(cv2image,(294,219), 40, (0,0,255), 2)
        cv2.line(cv2image,(250,219),(340,219),(0,255,0),1) #Horizontal
        cv2.line(cv2image,(294,175),(294,270),(255,100,255),1) #Linea vertical
        current_image = Image.fromarray(cv2image)  # convert image for PIL
        imgtk = ImageTk.PhotoImage(image=current_image)  # convert image for tkinter
        labelVideo.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
        labelVideo.config(image=imgtk)  # show the image
    Ventana_Calibrar.after(30, video_loop)  # call the same function after 30 milliseconds


def abrirVentanaMenuPrincipal():
    mainMenu = Tk()
    mainMenu.title("Main menu")
    mainMenu.geometry('1000x600')

    #Creacion de pestañas
    ###############
    pestañasFrame = ttk.Notebook(mainMenu) #Marco de las pestañas
    pestañaPrincipal = Frame(pestañasFrame) #Pestaña principal
    pestañaConexion = Frame(pestañasFrame) #Pestaña de las conexiones
    pestañaManual = Frame(pestañasFrame) #Pestaña de control manual
    pestañaAgregrarUsuario = Frame(pestañasFrame) #Pestaña agregar usuario
    #Agregamos las pestañas al frame principal y le damos el nombre
    pestañasFrame.add(pestañaPrincipal, text="Principal")
    pestañasFrame.add(pestañaManual, text="Manual")
    pestañasFrame.add(pestañaAgregrarUsuario, text="Agregar usuario")
    pestañasFrame.add(pestañaConexion, text="Conexiones")
    pestañasFrame.pack(expand=1, fill='both')
    ############



    #Widgets pestaña principal
    EtiquetaNombre=Label(pestañaPrincipal, text="Nombre:" , bg="light gray", fg= "white")
    EtiquetaNombre.pack(padx=5, pady=5, ipadx=5, ipady=5)
    TxtNombre=Entry(pestañaPrincipal)
    TxtNombre.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)

    EtiquetaDiametro=Label(pestañaPrincipal, text="Diametro:" , bg="light gray", fg= "white")
    EtiquetaDiametro.pack(padx=5, pady=5, ipadx=5, ipady=5)
    TxtDiametro=Entry(pestañaPrincipal)
    TxtDiametro.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)

    EtiquetaEspesor=Label(pestañaPrincipal, text="Espesor:" , bg="light gray", fg= "white")
    EtiquetaEspesor.pack(padx=5, pady=5, ipadx=5, ipady=5)
    TxtEspesor=Entry(pestañaPrincipal)
    TxtEspesor.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)

    EtiquetaLargo=Label(pestañaPrincipal, text="Largo:" , bg="light gray", fg= "white")
    EtiquetaLargo.pack(padx=5, pady=5, ipadx=5, ipady=5)
    TxtLargo=Entry(pestañaPrincipal)
    TxtLargo.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)

    ButtonIniciar=Button(pestañaPrincipal,text="Iniciar", fg="blue", state = 'normal') 
    ButtonIniciar.pack(side=BOTTOM)

    ButtonStop=Button(pestañaPrincipal,text="Stop", fg="blue", state = 'normal')
    ButtonStop.pack(side=BOTTOM)

    ButtonArchivoNuevo=Button(pestañaPrincipal,text="Archivo Nuevo +", fg="blue", state = 'normal', command = guardarArchivo)
    ButtonArchivoNuevo.pack(side=BOTTOM)

    ButtonCalibrar=Button(pestañaPrincipal,text="Archivo Nuevo +", fg="blue", state = 'normal', command = guardarArchivo)
    ButtonCalibrar.pack(side=BOTTOM)
    #Fin widgets pestaña principal


    #Widgets pestaña agregar usuario
    EtiquetaUsuario=Label(pestañaAgregrarUsuario, text="Usuario:" , bg="pink", fg= "white")
    EtiquetaUsuario.pack(padx=5, pady=5, ipadx=5, ipady=5)
    TxtUser=Entry(pestañaAgregrarUsuario)
    TxtUser.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)
    EtiquetaContra=Label(pestañaAgregrarUsuario, text="Contraseña:", bg="pink", fg= "white")
    EtiquetaContra.pack(padx=5, pady=5, ipadx=5, ipady=5)
    TxtPass=Entry(pestañaAgregrarUsuario)
    TxtPass.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)
    ButtonRegistrar=Button(pestañaAgregrarUsuario , text="Registrar", fg="blue", state = 'normal' , command=lambda:registroUsuario(TxtUser.get(), TxtPass.get()))
    
    ButtonRegistrar.pack(side=BOTTOM)
    #Fin widgets pestaña agregar usuario


    #Widgets ventana conexion
    e1=Label(pestañaConexion, text="Password:" , bg="pink", fg= "white")
    e1.pack(padx=5, pady=5, ipadx=5, ipady=5)
    entrada1=Entry(pestañaConexion)
    entrada1.pack(fill=X,padx=5,pady=58,ipadx=5, ipady=5)
    if hayInternet == False: #Comprueba si hay internet.
        ButtonInternet=Button(pestañaConexion,text="Por internet", fg="blue", state = 'disable' )
    else:
        ButtonInternet=Button(pestañaConexion,text="Por internet", fg="blue", state = 'normal' )

    ButtonInternet.pack(side=TOP)
    ButtonLocal=Button(pestañaConexion,text="Local", fg="blue")
    ButtonLocal.pack(side=BOTTOM)
    #Fin widgets ventana conexion

    
    #Widget Ventana calibrar
    Panel_Video = LabelFrame(pestañaManual, width=600, height=450, relief="sunken") #Panel que contiene la etiqueta donde hace el streaming del video.
    Panel_Video.place(x=10 , y=10)

    Panel_Avance = LabelFrame(pestañaManual, width=335, height=150, relief="sunken") #Panel que contiene el textbox y los radioButtons
    Panel_Avance.place(x=650, y=10)

    Panel_Flechas = LabelFrame(pestañaManual, width=335, height=400, relief="sunken") #Panel que contiene las flechas y los botones
    Panel_Flechas.place(x=650 , y=200)
   
    #Capture video frames
    global labelVideo
    labelVideo = Label(Panel_Video,  height=438,  width=588)
    labelVideo.place(x=2, y= 2)
    global cap 
    cap = cv2.VideoCapture(0)
    
    #imagenes de las flechas
    #global flechaArriba, flechaDerecha, flechaIzquierda, flechaAbajo
    flechaDerecha = PhotoImage(file='Python/Imagenes/flechaDerecha.png')
    flechaIzquierda = PhotoImage(file='Python/Imagenes/flechaIzquierda.png')
    flechaAbajo = PhotoImage(file='Python/Imagenes/flechaAbajo.png')
    flechaArriba  = tk.PhotoImage(file='Python/Imagenes/flechaArriba.png')

    #TextField de la cantidad de movimiento que se necesita para cada eje
    AvanceTxt = Entry(Panel_Avance)
    AvanceTxt.place(x=60, y=20)

    LabelAvance = Label(Panel_Avance, text = "Avance: ")
    LabelAvance.place(x=30, y=20)
 

    #RadioButton de las unidades de medida.
    global unidadMedida 
    unidadMedida = IntVar()
    RadioCentimetros = Radiobutton(Panel_Avance, text="Centimetros:" , variable=unidadMedida, value = 1).place(x=200 , y=10)
    RadioPulgadas = Radiobutton(Panel_Avance, text="Pulgadas: ", variable=unidadMedida, value = 2).place(x=200 , y=50)

    #Poner las imagenes a los
    
    ButtonDerecha = Button(Panel_Flechas, state = 'normal', image = flechaDerecha, command = lambda: obtenerRadioButton(AvanceTxt.get(),1)).place(x=200, y=50)
    
    ButtonIzquierda=Button(Panel_Flechas,text="Izquierda", fg="blue", state = 'normal', image=flechaIzquierda , command = lambda: obtenerRadioButton(AvanceTxt.get(),2)).place(x=50, y=50)
    ButtonAbajo=Button(Panel_Flechas,text="Derecha", fg="blue", state = 'normal', image=flechaAbajo , command = lambda: obtenerRadioButton(AvanceTxt.get(),3)).place(x=150, y=100)
    ButtonArriba=Button(Panel_Flechas,text="Izquierda", fg="blue", state = 'normal', image=flechaArriba , command = lambda: obtenerRadioButton(AvanceTxt.get(),4)).place(x=150, y=10)
    
    ButtonAbajoZ=Button(Panel_Flechas,text="Derecha Z", fg="blue", state = 'normal', image=flechaAbajo , command = lambda: obtenerRadioButton(AvanceTxt.get(),6)).place(x=20, y=200)
    ButtonArribaZ=Button(Panel_Flechas,text="Izquierda Z", fg="blue", state = 'normal', image=flechaArriba , command = lambda: obtenerRadioButton(AvanceTxt.get(),5)).place(x=250, y=200)


    ButtonIniciar=Button(Panel_Flechas, text="Iniciar",  state = 'normal' , width = "5" , height= "2", background ="green" , command = video_loop).place(x=250, y=330)
    ButtonParar=Button(Panel_Flechas, text="Parar", state = 'normal',background ="red", width = "5" , height= "2", command = lambda: obtenerRadioButton(AvanceTxt.get(),5)).place(x=50, y=330)
    #Fin widgets vetntana calibrar
    
    mainMenu.mainloop()
    
 

#crea y llama a las ventanas secundarias(FIN).
#######################
   
if __name__ == '__main__':

    #Creacion del login
    loginWindow.title("Login")
    loginWindow.geometry('1000x600')
    loginWindow.configure(background='dark gray')
    loginWindow.resizable(0,0)
        #
    EtiquetaUsuario=Label(loginWindow, text="Usuario:" , bg="pink", fg= "white")
    EtiquetaUsuario.pack(padx=5, pady=5, ipadx=5, ipady=5)
    TxtUsuario=Entry(loginWindow)
    TxtUsuario.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)

    EtiquetaContra=Label(loginWindow, text="Contraseña:" , bg="pink", fg= "white")
    EtiquetaContra.pack(padx=5, pady=5, ipadx=5, ipady=5)
    TxtContra=Entry(loginWindow)
    TxtContra.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)

    ButtonVerificar=Button(loginWindow,text="Verificar", fg="blue", state = 'normal' , command=lambda:verificarUsuario(TxtUsuario.get(), TxtContra.get()))

    ButtonVerificar.pack(side=BOTTOM)
    #Fin del login



    #Crea una ventana hija del loginWindow
    splashScreen=Toplevel(loginWindow)
    splashScreen.title("Splash Screen")
    splashScreen.geometry("1000x600")
    splashScreen.config(bg="black")
    splashScreen.protocol("WM_DELETE_WINDOW", "onexit")
    splashScreen.resizable(0,0)

    #Ocultamos loginWindow
    ocultar(loginWindow)
    ocultar(mainMenu)


    #iniciamos la aplicacion abriendo el splash y manteniendo oculto el menu despues de 4000 milisegundos.
    splashScreen.after(4000,cerrar_splashscreen)

    #Agregamos una etiqueta al splash.
    #Label(splashScreen,text="BIENVENIDO A NUESTRA APLICACIÓN",bg="black",fg="white",font=(15)).pack()

    imagen=PhotoImage(file="Python/Imagenes/chavito.gif")
    foto=Label(splashScreen, image = imagen,).pack(side=TOP)
    #ProgressBar started
    maxValue=100
    progressbar=ttk.Progressbar(splashScreen,orient="horizontal",length=300,mode="determinate")
    progressbar.pack(side=BOTTOM)
    currentValue=0
    progressbar["value"]=currentValue
    progressbar["maximum"]=maxValue
    divisions=10
    for i in range(divisions):
        currentValue=currentValue+20
        progressbar.after(500, progress(currentValue))
        # Force an update of the GUI
        progressbar.update()
    #ProgressBar finished.

    

    loginWindow.mainloop()