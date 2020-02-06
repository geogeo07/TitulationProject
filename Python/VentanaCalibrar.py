import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk #Galeria para las imagenes


#Librerias para usar los puertos GPIO
from time import sleep
#import RPi.GPIO as gpio



'''
Configuracion de los motores
'''
 #Sentido del giro
CW = 1 #Horario
CCW = 0 #Antihorario

#Eje x
DIRx = 20
STEPx = 21
#Eje y
DIRy = 19
STEPy = 26
#Eje z
DIRz = 13
STEPz = 21
#Eje 
DIRw = 20
STEPw = 21


'''
gpio.setwarnings(False) #Para que no mande alarmas.
gpio.setmode(gpio.BCM) #Modo de conexion y numeracion de los pines.

#Configuramos los pines como salidas.
gpio.setup(DIRx, gpio.OUT) 
gpio.setup(STEPx, gpio.OUT)
gpio.setup(DIRy, gpio.OUT) 
gpio.setup(STEPy, gpio.OUT)
gpio.setup(DIRz, gpio.OUT) 
gpio.setup(STEPz, gpio.OUT)

'''


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
 
def activarCamara():
    '''
    Extrae el texto de la etiqueta y lo compara para ver si prende o apaga la camara.
    '''
    accion = BotonPrenderCamara.cget('text') #Consigue el atributo elegido del boton
    print(accion)
    if accion == "Prender camara":
        labelVideo.place(x=2, y= 2)
        BotonPrenderCamara['text'] = 'Apagar camara'
        cap = cv2.VideoCapture(0)
        video_loop()
    if accion == "Apagar camara":
        print("apagar la camara porfa")
        BotonPrenderCamara['text'] = 'Prender camara'        
        cap.release()

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
 

def moverMotor(unidades, Avance, direccion):
       
    '''
    #Recibe las unidades de medida, el avance(lo que contiene el textbox) y la direccion (el motor que se movera),
    #despues hace la conversion (en caso de necesitarla) a pulgadas y despues activa los puertos gpio para mover el motor.
    #Direccion: 1 Motor x+, 2 Hacia Motor x-, 3 Motor y+, 4 Motor y-, 5 Motor z+, 6 Motor z-.
    #Unidades: 1=Centimetros,  2= Pulgadas.
    

    print ("Unidades" + unidades)
    if unidades == "Centimetros":
        distancia = float(Avance)*1
        print("La distancia es: ")
        print(distancia)
    else:
        distancia = float(Avance)*2.54 
        print("La distancia es: ")
        print(distancia)


    if direccion == 1:
        #Mover el motor de x +
        try:
            gpio.output(DIRx,CW)
            for x in range(distancia):
                gpio.output(STEPx,gpio.HIGH)
                sleep(.0100)
                gpio.output(STEPx,gpio.LOW)
                sleep(.0100)
        except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
            print("Cleaning up!")
            gpio.cleanup()
        
    print("unidades = ")
    print(unidades)
    print("distancia = ")
    print(distancia)
    print("direccion = ")
    print(direccion)

    if direccion == 2:
        #Mover el motor de x -
        try:
            gpio.output(DIRx,CCW)
            for x in range(distancia):
                gpio.output(STEPx,gpio.HIGH)
                sleep(.0100)
                gpio.output(STEPx,gpio.LOW)
                sleep(.0100)
        except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
            print("Cleaning up!")
            gpio.cleanup()

    print("unidades = ")
    print(unidades)
    print("distancia = ")
    print(distancia)
    print("direccion = ")
    print(direccion)
    
    if direccion == 3:
        #Mover el motor de y +
        try:
            gpio.output(DIRy,CW)
            for x in range(distancia):
                gpio.output(STEPy,gpio.HIGH)
                sleep(.0100)
                gpio.output(STEPy,gpio.LOW)
                sleep(.0100)
        except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
            print("Cleaning up!")
            gpio.cleanup()

    print("unidades = ")
    print(unidades)
    print("distancia = ")
    print(distancia)
    print("direccion = ")
    print(direccion)
    
    if direccion == 4:
        #Mover el motor de y -
       try:
            gpio.output(DIRy,CCW)
            for x in range(distancia):
                gpio.output(STEPy,gpio.HIGH)
                sleep(.0100)
                gpio.output(STEPy,gpio.LOW)
                sleep(.0100)

        except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and 
            print("Cleaning up!")
            gpio.cleanup()

    print("unidades = ")
    print(unidades)
    print("distancia = ")
    print(distancia)
    print("direccion = ")
    print(direccion)
    
    if direccion == 5:
        #Mover el motor de z +
        try:
            gpio.output(DIRz,CW)
            for x in range(distancia):
                gpio.output(STEPz,gpio.HIGH)
                sleep(.0100)
                gpio.output(STEPz,gpio.LOW)
                sleep(.0100)
        except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
            print("Cleaning up!")
            gpio.cleanup()

    print("unidades = ")
    print(unidades)
    print("distancia = ")
    print(distancia)
    print("direccion = ")
    print(direccion)
    
    
    if direccion ==6:
        #Mover el motor de z -
        try:
            gpio.output(DIRz,CCW)
            for x in range(distancia):
                gpio.output(STEPz,gpio.HIGH)
                sleep(.0100)
                gpio.output(STEPz,gpio.LOW)
                sleep(.0100)
        except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
            print("Cleaning up!")
            gpio.cleanup()

    print("unidades = ")
    print(unidades)
    print("distancia = ")
    print(distancia)
    print("direccion = ")
    print(direccion)
    
'''



def abrirVentanaCalibrar():
#Configuraciones de la ventana
    global Ventana_Calibrar
    Ventana_Calibrar = tk.Tk()  #Makes main ventanaCalibrar
    Ventana_Calibrar.iconbitmap("Python/Imagenes/icono.ico")
    Ventana_Calibrar.wm_title("Calibracion manual")
    Ventana_Calibrar.config(background="#FFFFFF")
    Ventana_Calibrar.geometry("1000x600")

#Paneles
    Panel_Video = tk.LabelFrame(Ventana_Calibrar, width=600, height=450, relief="sunken") #Panel que contiene la etiqueta donde hace el streaming del video.
    Panel_Video.place(x=10 , y=10)

    Panel_Avance = tk.LabelFrame(Ventana_Calibrar, width=335, height=150, relief="sunken") #Panel que contiene el textbox y los radioButtons
    Panel_Avance.place(x=650, y=10)

    Panel_Flechas = tk.LabelFrame(Ventana_Calibrar, width=335, height=400, relief="sunken") #Panel que contiene las flechas y los botones
    Panel_Flechas.place(x=650 , y=200)

    
    global labelVideo
    global cap 
    #Capture video frames
    cap = cv2.VideoCapture(0)
    labelVideo = tk.Label(Panel_Video,  height=438,  width=588) #Etiqueta donde anexamos el stream de la camara.
    
    Etiqueta_PosicionX = tk.Label(Panel_Video, text = "Posicion X: ")
    Etiqueta_PosicionY = tk.Label(Panel_Video, text = "Posicion Y: ")
    Etiqueta_PosicionZ = tk.Label(Panel_Video, text = "Posicion Z: ")
    Etiqueta_PosicionX.place(x=10, y=10)
    Etiqueta_PosicionY.place(x=10, y=50)
    Etiqueta_PosicionZ.place(x=10, y=100)


    global BotonPrenderCamara
    BotonPrenderCamara= tk.Button(Ventana_Calibrar , text = "Prender camara",  command =  activarCamara, width=10 , height = 3)
    BotonPrenderCamara.place(x=50 , y=500)

     


    
    #imagenes de las flechas
    flechaDerecha = tk.PhotoImage(file='Python/Imagenes/flechaDerecha.png')
    flechaIzquierda = tk.PhotoImage(file='Python/Imagenes/flechaIzquierda.png')
    flechaAbajo = tk.PhotoImage(file='Python/Imagenes/flechaAbajo.png')
    flechaArriba  = tk.PhotoImage(file='Python/Imagenes/flechaArriba.png')

    #TextField de la cantidad de movimiento que se necesita para cada eje
    AvanceTxt = tk.Entry(Panel_Avance)
    AvanceTxt.place(x=60, y=20)

    LabelAvance = tk.Label(Panel_Avance, text = "Avance: ")
    LabelAvance.place(x=30, y=20)


    #RadioButton de las unidades de medida.
    global unidadMedida 
    unidadMedida = tk.IntVar()
    RadioCentimetros = tk.Radiobutton(Panel_Avance, text="Centimetros:" , variable=unidadMedida, value = 1).place(x=200 , y=10)
    RadioPulgadas = tk.Radiobutton(Panel_Avance, text="Pulgadas: ", variable=unidadMedida, value = 2).place(x=200 , y=50)

 

    ButtonDerecha=tk.Button(Panel_Flechas,text="Derecha", fg="blue", state = 'normal', image=flechaDerecha , command = lambda: obtenerRadioButton(AvanceTxt.get(),1)).place(x=200, y=50)
    ButtonIzquierda=tk.Button(Panel_Flechas,text="Izquierda", fg="blue", state = 'normal', image=flechaIzquierda , command = lambda: obtenerRadioButton(AvanceTxt.get(),2)).place(x=50, y=50)
    ButtonAbajo=tk.Button(Panel_Flechas,text="Derecha", fg="blue", state = 'normal', image=flechaAbajo , command = lambda: obtenerRadioButton(AvanceTxt.get(),3)).place(x=150, y=100)
    ButtonArriba=tk.Button(Panel_Flechas,text="Izquierda", fg="blue", state = 'normal', image=flechaArriba , command = lambda: obtenerRadioButton(AvanceTxt.get(),4)).place(x=150, y=10)

    ButtonAbajoZ=tk.Button(Panel_Flechas,text="Derecha Z", fg="blue", state = 'normal', image=flechaAbajo , command = lambda: obtenerRadioButton(AvanceTxt.get(),6)).place(x=20, y=200)
    ButtonArribaZ=tk.Button(Panel_Flechas,text="Izquierda Z", fg="blue", state = 'normal', image=flechaArriba , command = lambda: obtenerRadioButton(AvanceTxt.get(),5)).place(x=250, y=200)


    ButtonIniciar=tk.Button(Panel_Flechas, text="Iniciar",  state = 'normal' , width = "5" , height= "2", background ="green" , command = video_loop).place(x=250, y=330)
    ButtonParar=tk.Button(Panel_Flechas, text="Parar", state = 'normal',background ="red", width = "5" , height= "2", command = lambda: obtenerRadioButton(AvanceTxt.get(),5)).place(x=50, y=330)

    #manda a llamar la funcion para transmitir el video.
    #video_loop() 

    Ventana_Calibrar.mainloop()  #Starts GUI

abrirVentanaCalibrar()


