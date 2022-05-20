from tkinter import Tk, Label, Entry
from PIL import ImageTk, Image
from captcha.image import ImageCaptcha
from tkinter import ttk
from random import SystemRandom, random
from tkinter import messagebox
import subprocess as sp
from numpy import imag

root = Tk()
root.title("CAPTCHA")
root.geometry("400x300+750+300")
root.iconbitmap(default="../resources/Icono_captcha.ico")

titulo_captcha = Label(text="Por favor, \n introduzca el captcha: ",font=("Arial",15))
titulo_captcha.grid(padx=100,pady=10,columnspan=2)

'''
longitud = 6
valores = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
cryptogen = SystemRandom()
captcha_generado = ""
while longitud > 0: 
        captcha_generado = captcha_generado + cryptogen.choice(valores)
        longitud = longitud - 1
'''

captcha_generado = "XDHujA"
image = ImageCaptcha(width=300,height=200)
palabra = (captcha_generado)
'''image = image.generate_image(palabra)
image.save('Captcha.png')'''


captcha_texto = palabra
print(captcha_texto)
captcha_teclado = Entry(textvariable=captcha_texto)
captcha_teclado.grid(column=1, row=1)

def comprobar():
    if captcha_texto == captcha_teclado.get():
        messagebox.showinfo("Captcha correcto",f"Ha introducido correctamente el código")
        sp.Popen("SecureRoomUI.exe")
        root.destroy()
    else:
        messagebox.showinfo("Captcha erróneo",f"Ha introducido el código erróneo")

iniciarSesionButton = ttk.Button(text="Validad Captcha",command=comprobar)
iniciarSesionButton.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=40)

image_captcha = ImageTk.PhotoImage(Image.open('../resources/Captcha.png').resize((150,150)))
label_image = Label(image=image_captcha).place(x=50,y=100)


root.mainloop()