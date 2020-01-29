from tkinter import *
import os

def verificarUsuario(username, contra):
#def verificarUsuario(ventana, username, contra):  Ventana es el nombre de la ventana que sera abierta
    #Recibe como parametro el usuario y la contra, abre el documento donde estan
    #guardadas los usuarios y si lo encuentra, permite el ingreso, sino manda un mensaje de error.
    
    usuario_info = username
    contra_info = contra

    if usuario_info == '' or contra_info == '':
        messagebox.showwarning("Cuidado", "Revisa tus datos bro")
        
    else:
        print(usuario_info, contra_info)
        lista_archivos = os.listdir()
      
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
                Ventana_Login.destroy()
            else:
                messagebox.showwarning("Cuidado", "Password incorrecto")
        else:
            messagebox.showwarning("Cuidado", "Usuario incorrecto")


def abrirVentanaLogin():
    #Creacion del login
    Ventana_Login = Tk()

    Ventana_Login.title("Login")
    Ventana_Login.geometry('380x380')
    Ventana_Login.configure(background='dark gray')
    Ventana_Login.resizable(0,0)
        #
    EtiquetaUsuario=Label(Ventana_Login, text="Usuario:" , bg="pink", fg= "white")
    EtiquetaUsuario.pack(padx=5, pady=5, ipadx=5, ipady=5)
    TxtUsuario=Entry(Ventana_Login)
    TxtUsuario.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)

    EtiquetaContra=Label(Ventana_Login, text="Contraseña:" , bg="pink", fg= "white")
    EtiquetaContra.pack(padx=5, pady=5, ipadx=5, ipady=5)
    TxtContra=Entry(Ventana_Login)
    TxtContra.pack(fill=X,padx=5,pady=5,ipadx=5, ipady=5)

    ButtonVerificar=Button(Ventana_Login,text="Verificar", fg="blue", state = 'normal' , command=lambda:verificarUsuario(TxtUsuario.get(), TxtContra.get()))

    ButtonVerificar.pack(side=BOTTOM)

    Ventana_Login.mainloop()