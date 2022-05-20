
from tkinter import Y, StringVar
from tkinter import Label
from tkinter import Frame
from tkinter import Entry
from tkinter import Tk

from tkinter import ttk as ttk
from tkinter import messagebox as MessageBox

from random import SystemRandom

from tkinter import messagebox
import subprocess 

root = Tk()


nombreUsuario = StringVar()
contraUsuario = StringVar()


def createGUI():
    # ventana principal
    
    root.title("Login Usuario")
    root.geometry("500x500+700+200")
    root.iconbitmap(default="../resources/User.ico")
    # mainFrame
    mainFrame = Frame(root)
    mainFrame.pack()
    mainFrame.config(width=480,height=320)

    # textos y titulos
    titulo = Label(mainFrame,text="Login de Usuario",font=("Arial",24))
    titulo.grid(padx=10,pady=70,columnspan=2)

    nombreLabel = Label(mainFrame,text="Nombre: ", font=("Arial",15))
    nombreLabel.grid(row=1)

    passLabel = Label(mainFrame,text="Contraseña: ", font=("Arial",14))
    passLabel.grid(row=2)

    #GENERADOR DE USUARIOS
    longitud = 4
    valores = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cryptogen = SystemRandom()
    usuario = ""
    while longitud > 0:
        usuario = usuario + cryptogen.choice(valores)
        longitud = longitud - 1
    
    messagebox.showinfo("USUARIO GENERADO",f"Su usuario: " + usuario)

    #GENERADOR DE CLAVE
    longitud = 2
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

    cryptogen = SystemRandom()
    clave = ""
    while longitud > 0:
        clave = clave + cryptogen.choice(valores)
        longitud = longitud - 1
    
    messagebox.showinfo("CLAVE GENERADA",f"Su clave: " + clave)


    nombreUsuario = usuario
    print(nombreUsuario)
    nombre_teclado = Entry(mainFrame,textvariable=nombreUsuario)
    nombre_teclado.grid(column=1,row=1)
    
    
    
    contraUsuario = clave
    print(contraUsuario)
    contra_teclado = Entry(mainFrame,textvariable=contraUsuario,show="*")
    contra_teclado.grid(column=1,row=2)

   
    #Iniciar sesión
   
    def iniciarSesion():
        if nombreUsuario == nombre_teclado.get():
            if contraUsuario == contra_teclado.get():
                MessageBox.showinfo("Conectado",f"Se inicio sesion con el usuario {nombreUsuario} con EXITO!!!")
                
                root.destroy()
                
        else:
            MessageBox.showerror("Error","Usuario o contraseña incorrecta")
            return

    

    # botones
    iniciarSesionButton = ttk.Button(mainFrame,text="Iniciar Sesión",command=iniciarSesion)
    iniciarSesionButton.grid(column=1,row=3,ipadx=5,ipady=5,padx=5,pady=40)


    root.mainloop()

    subprocess.Popen(["Captcha.exe"])

    
    

if __name__=="__main__":
   
    createGUI()



