from tkinter import *
from tkinter import ttk 


mainWindow = Tk()

mainWindow.title("Main Window con pestañas")
mainWindow.geometry("500x300")

pestañasFrame = ttk.Notebook(mainWindow) #Marco de las pestañas

pestañaPrincipal = Frame(pestañasFrame) #Pestaña principal
pestañaConexion = Frame(pestañasFrame) #Pestaña de las conexiones

pestañasFrame.add(pestañaPrincipal, text="Principal")
pestañasFrame.add(pestañaConexion, text="Conexiones")

pestañasFrame.pack(expand=1, fill='both')

mainWindow.mainloop()