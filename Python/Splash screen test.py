from tkinter import *
from tkinter import ttk

#from PIL import ImageTk, Image

mainMenu=Tk()
#imagen1 = ImageTk.PhotoImage(Image.open("chavito.jpg"))
#label1 = Label(mainMenu, image=imagen1)
#label1.grid(row=1,column=1)



def imprimir(texto):
     print (texto)

def mostrar(ventana):
     return ventana.deiconify # Muestra una ventana

def ocultar(ventana):
     return ventana.withdraw() # Oculta una ventana

def ejecutar(f): 
    mainMenu.after(100, f)


def cerrar_splashscreen():
    ejecutar(ocultar(splashScreen))
    ejecutar(mostrar(mainMenu))


def progress(currentValue): #Llama
    progressbar["value"]=currentValue






#Creacion del menu
menu1 = Menu(mainMenu)
mainMenu.config(menu=menu1)
menu1_1 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="AMARILLO", menu=menu1_1)
menu1_1_1 = Menu(menu1_1, tearoff=0)
menu1_1.add_cascade(label="FRUTAS", menu=menu1_1_1)
menu1_1_1.add_command(label="BANANO",command=lambda: imprimir("BANANO"))
menu1_1_1.add_command(label="PIÑA",command=lambda: imprimir("PIÑA"))

menu1_2 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="ROJO", menu=menu1_2)
menu1_2.add_command(label="SANGRE",command=lambda: imprimir("SANGRE"))
menu1_2.add_separator()
menu1_2_1 = Menu(menu1_2, tearoff=0)
menu1_2.add_cascade(label="FRUTAS", menu=menu1_2_1)
menu1_2_1.add_command(label="FRESA",command=lambda: imprimir("FRESA"))
menu1_2_1.add_command(label="MANZANA",command=lambda: imprimir("PIÑA") )

#Crea una ventana hija del mainMenu
splashScreen=Toplevel(mainMenu)
splashScreen.geometry("400x200")
splashScreen.config(bg="black")
splashScreen.protocol("WM_DELETE_WINDOW", "onexit")
splashScreen.resizable(0,0)

#Ocultamos mainMenu
ocultar(mainMenu)

#iniciamos la aplicacion abriendo el splash y manteniendo oculto el menu despues de 4000 milisegundos.
splashScreen.after(4000,cerrar_splashscreen)

#Agregamos una etiqueta al splash.
Label(splashScreen,text="BIENVENIDO A NUESTRA APLICACIÓN",bg="black",fg="white",font=(15)).pack()



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



#Creamos la ventana del login



#ocultar(splashScreen)







mainMenu.mainloop()



