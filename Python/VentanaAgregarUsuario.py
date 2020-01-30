from tkinter import *
from tkinter import messagebox


def registroUsuario(username, contra):
    #Recibe como parametros el usuario y la contraseña ingresados, abre el documento de usuarios
    #y los guarda ahi.

    usuario_info = username
    contra_info = contra
    file = open("Python/Archivos/usuario_info.txt", "a") #Ruta del archivo "a" para poder escribir y leer en el archivo.
    file.write(usuario_info + "\n")
    file.write(contra_info + "\n")
    file.close()
    messagebox.showinfo("Listo","Quedaste registrado")

def abrirVentanaAgregarUsuario():
    
    global Ventana_AgregarUsuario 
    Ventana_AgregarUsuario = Tk()

    Ventana_AgregarUsuario.title("Agregar usuario")
    Ventana_AgregarUsuario.geometry('380x380')
    Ventana_AgregarUsuario.configure(background='dark gray')
    Ventana_AgregarUsuario.resizable(0,0)
    
    EtiquetaUsuario=Label(Ventana_AgregarUsuario, text="Usuario:" , bg="pink", fg= "white")
    EtiquetaUsuario.pack(padx=5, pady=5, ipadx=5, ipady=5)
    TxtUser=Entry(Ventana_AgregarUsuario)
    TxtUser.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)
    EtiquetaContra=Label(Ventana_AgregarUsuario, text="Contraseña:", bg="pink", fg= "white")
    EtiquetaContra.pack(padx=5, pady=5, ipadx=5, ipady=5)
    TxtPass=Entry(Ventana_AgregarUsuario)
    TxtPass.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)
    ButtonRegistrar=Button(Ventana_AgregarUsuario,text="Registrar", fg="blue", state = 'normal' , command=lambda:registroUsuario(TxtUser.get(), TxtPass.get()))
    
    ButtonRegistrar.pack(side=BOTTOM)

    Ventana_AgregarUsuario.mainloop()