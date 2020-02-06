from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import ImageTk, Image 
import os

from tkinter import filedialog

import socket
from urllib.request import urlopen



def hayInternet(): #Comprueba que exista alguna conexion a internet.
   try:
        response = urlopen('https://www.google.com/', timeout=10)
        return True
   except: 
        return False

def abrirVentanaConexion():
    Ventana_Conexion = Tk()
    #Widgets ventana conexion
    Etiqueta=Label(Ventana_Conexion, text="Password:" , bg="pink", fg= "white")
    Etiqueta.pack(padx=5, pady=5, ipadx=5, ipady=5)
    entrada1=Entry(Ventana_Conexion)
    entrada1.pack(fill=X,padx=5,pady=58,ipadx=5, ipady=5)
    if hayInternet == False: #Comprueba si hay internet.
        ButtonInternet=Button(Ventana_Conexion,text="Por internet", fg="blue", state = 'disable' )
    else:
        ButtonInternet=Button(Ventana_Conexion,text="Por internet", fg="blue", state = 'normal' )

    ButtonInternet.pack(side=TOP)
    ButtonLocal=Button(Ventana_Conexion,text="Local", fg="blue")
    ButtonLocal.pack(side=BOTTOM)
    #Fin widgets ventana conexion
    VentanaConexion.mainloop()