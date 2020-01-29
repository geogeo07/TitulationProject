from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

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

#Creacion del login
loginWindow.title("Login")
loginWindow.geometry('380x380')
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

ButtonVerificar=Button(loginWindow,text="Verificar", fg="blue", state = 'normal' , command=lambda:verificarUsuario(mainMenu, TxtUsuario.get(), TxtContra.get()))

ButtonVerificar.pack(side=BOTTOM)



#Crea una ventana hija del loginWindow
splashScreen=Toplevel(loginWindow)
splashScreen.title("Splash Screen")
splashScreen.geometry("400x200")
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



#Creacion del menu
menuPrincipal = Menu(mainMenu)
mainMenu.title("Main menu")
mainMenu.geometry('380x480')
mainMenu.config(menu=menuPrincipal)


menu1 = Menu(menuPrincipal, tearoff=0)
menuPrincipal.add_cascade(label="File", menu=menu1)


menu1_1 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Archivo nuevo", menu=menu1_1)
menu1_1.add_command(label="Ingresar valores")
menu1_1.add_command(label="Limpiar")

menu1_2 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Abrir", menu=menu1_2)
menu1_2.add_command(label="Abrir codigo")





menu2_1 = Menu(menuPrincipal, tearoff=0)

menuPrincipal.add_cascade(label="Ventana manual", menu=menu2_1)
menu2_1.add_command(label="Valores manuales")


menu3_1 = Menu(menuPrincipal, tearoff=0)

menuPrincipal.add_cascade(label="Agregar Usuario", menu=menu3_1)
menu3_1.add_command(label="Agregar nuevo Usuario")


menu4_1 = Menu(menuPrincipal, tearoff=0)

menuPrincipal.add_cascade(label="Conexion", menu=menu4_1)
menu4_1.add_command(label="Conexion")
menu4_1.add_command(label="Internet")


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

ButtonArchivoNuevo=Button(pestañaPrincipal,text="Archivo Nuevo +", fg="blue", state = 'normal')
ButtonArchivoNuevo.pack(side=BOTTOM)

ButtonCalibrar=Button(pestañaPrincipal,text="Archivo Nuevo +", fg="blue", state = 'normal')
ButtonCalibrar.pack(side=BOTTOM)
#Fin widgets pestaña principal



loginWindow.mainloop()
    
    
    
    







