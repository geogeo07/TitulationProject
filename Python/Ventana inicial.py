from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

from tkinter import filedialog


import socket
from urllib.request import urlopen




def imprimir(texto):
     print (texto)

def registroUsuario(username, contra):
    usuario_info = username
    contra_info = contra
    file = open("usuario_info.txt", "w")
    file.write(usuario_info + "\n")
    file.write(contra_info)
    file.close()



def verificarUsuario(ventana, username, contra):
    
    usuario_info = username
    contra_info = contra

    if usuario_info == '' or contra_info == '':
        messagebox.showwarning("Cuidado", "Revisa tus datos bro")
        
    else:
        print(usuario_info, contra_info)

        lista_archivos = os.listdir()
    #print(lista_archivos, sep=' ', end='\n', file=sys.stdout, flush=False) Imprimir lista de archivos.

   
        archivo = open("usuario_info.txt", "r")
        verificar = archivo.read().splitlines()
        print(verificar)
        if usuario_info in verificar:
            posicion = verificar.index(usuario_info)
            print (usuario_info)
            print(posicion)
            print(contra_info)
            if contra in verificar[posicion+1]:
                messagebox.showinfo("Listo", "Ya quedo bro")
                ventana.deiconify()
                #menuPrincipal.destroy()
            else:
                messagebox.showwarning("Cuidado", "Password incorrecto")
        else:
            messagebox.showwarning("Cuidado", "Usuario incorrecto")
         

def hayInternet(): #Comprueba que exista alguna conexion a internet.
   try:
        response = urlopen('https://www.google.com/', timeout=10)
        return True
   except: 
        return False



 #######################
 #crea y llama a las ventanas secundarias(INICIO).       

def abrirVentanaInternet ():
    ventanaInternet = Toplevel(mainMenu)
    ventanaInternet.title("Internet Window")
    ventanaInternet.geometry('380x380')
    ventanaInternet.configure(background='dark gray')
   
    ventanaInternet.resizable(0,0)
    e1=Label(ventanaInternet, text="Password:" , bg="pink", fg= "white")
    e1.pack(padx=5, pady=5, ipadx=5, ipady=5)
    entrada1=Entry(ventanaInternet)
    entrada1.pack(fill=X,padx=5,pady=58,ipadx=5, ipady=5)
    if hayInternet == False: #Comprueba si hay internet.
        ButtonInternet=Button(ventanaInternet,text="Por internet", fg="blue", state = 'disable' )
    else:
        ButtonInternet=Button(ventanaInternet,text="Por internet", fg="blue", state = 'normal' )

    ButtonInternet.pack(side=TOP)
    ButtonLocal=Button(ventanaInternet,text="Local", fg="blue")
    ButtonLocal.pack(side=BOTTOM)


def abrirVentanaIngresarValores():
    #Vetana de agregar usuario
    ventanaIngresarValores = Toplevel(mainMenu)
    
    ventanaIngresarValores.title("Abrir Codigo")
    ventanaIngresarValores.geometry('380x380')
    ventanaIngresarValores.configure(background='dark gray')

    ventanaIngresarValores.resizable(0,0)



def llenarInicio(ruta):
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
    ruta=filedialog.askopenfilename(initialdir="/Proyecto de Titulacion (Python)", title ="Seleccione archivo", filetypes=(("txt files", "*.txt"), ("all files","*.*")))
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


    
    
    
        
    


    
    



def abrirVentanaAgregarUsuario ():
    #Vetana de agregar usuario
    ventanaAgregarUsuario = Toplevel(mainMenu)
    
    ventanaAgregarUsuario.title("Agregar usuario")
    ventanaAgregarUsuario.geometry('380x380')
    ventanaAgregarUsuario.configure(background='dark gray')

    ventanaAgregarUsuario.resizable(0,0)
    #
    EtiquetaUsuario=Label(ventanaAgregarUsuario, text="Usuario:" , bg="pink", fg= "white")
    EtiquetaUsuario.pack(padx=5, pady=5, ipadx=5, ipady=5)
    TxtUser=Entry(ventanaAgregarUsuario)
    TxtUser.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)

    EtiquetaContra=Label(ventanaAgregarUsuario, text="Contraseña:", bg="pink", fg= "white")
    EtiquetaContra.pack(padx=5, pady=5, ipadx=5, ipady=5)
    TxtPass=Entry(ventanaAgregarUsuario)
    TxtPass.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)
    ButtonRegistrar=Button(ventanaAgregarUsuario,text="Registrar", fg="blue", state = 'normal' , command=lambda:registroUsuario(TxtUser.get(), TxtPass.get()))
    
    ButtonRegistrar.pack(side=BOTTOM)
    #Fin ventana agregar usuario

#crea y llama a las ventanas secundarias(FIN).
#######################


mainMenu=Tk()

menuPrincipal = Menu(mainMenu)
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
menu1_2.add_command(label="Abrir codigo",command=abrirArchivo)





menu2_1 = Menu(menuPrincipal, tearoff=0)

menuPrincipal.add_cascade(label="Ventana manual", menu=menu2_1)
menu2_1.add_command(label="Valores manuales")


menu3_1 = Menu(menuPrincipal, tearoff=0)

menuPrincipal.add_cascade(label="Agregar Usuario", menu=menu3_1)
menu3_1.add_command(label="Agregar nuevo Usuario")


menu4_1 = Menu(menuPrincipal, tearoff=0)

menuPrincipal.add_cascade(label="Conexion", menu=menu4_1)
menu4_1.add_command(label="Conexion")
if hayInternet == False:
    menu4_1.add_command(label="Internet", state = 'disable')
else: 
    menu4_1.add_command(label="Internet")

EtiquetaNombre=Label(mainMenu, text="Nombre:" , bg="light gray", fg= "white")
EtiquetaNombre.pack(padx=5, pady=5, ipadx=5, ipady=5)
TxtNombre=Entry(mainMenu)
TxtNombre.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)

EtiquetaDiametro=Label(mainMenu, text="Diametro:" , bg="light gray", fg= "white")
EtiquetaDiametro.pack(padx=5, pady=5, ipadx=5, ipady=5)
TxtDiametro=Entry(mainMenu)
TxtDiametro.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)

EtiquetaEspesor=Label(mainMenu, text="Espesor:" , bg="light gray", fg= "white")
EtiquetaEspesor.pack(padx=5, pady=5, ipadx=5, ipady=5)
TxtEspesor=Entry(mainMenu)
TxtEspesor.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)

EtiquetaLargo=Label(mainMenu, text="Largo:" , bg="light gray", fg= "white")
EtiquetaLargo.pack(padx=5, pady=5, ipadx=5, ipady=5)
TxtLargo=Entry(mainMenu)
TxtLargo.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)

ButtonIniciar=Button(mainMenu,text="Iniciar", fg="blue", state = 'normal') 
ButtonIniciar.pack(side=BOTTOM)

ButtonStop=Button(mainMenu,text="Stop", fg="blue", state = 'normal')
ButtonStop.pack(side=BOTTOM)

ButtonArchivoNuevo=Button(mainMenu,text="Archivo Nuevo +", fg="blue", state = 'normal', command = guardarArchivo)
ButtonArchivoNuevo.pack(side=BOTTOM)




 



mainMenu.mainloop()