from asyncio import subprocess
from re import X
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
import os
import shutil
import time
import subprocess as sp
import win32api

from cv2 import destroyWindow


class Screen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Control Panel")
        self.root.wm_overrideredirect(True)
        self.root.geometry("500x500+700+200")
        
        self.root.iconphoto(False, tk.PhotoImage(file='../resources/icono.gif'))


        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both",expand=True)

        self.image_label = tk.Label(self.main_frame,image="")
        self.image_label.pack()

        os.mkdir('gif_frames')
        self.start = time.time()

        self.gif_frames = []
        self.images = []
        self.animation()
        self.root.mainloop()

        

    def animation(self):
        gif = Image.open('../resources/foto.gif')
        self.no_of_frames = gif.n_frames

        for i in range(self.no_of_frames):
            gif.seek(i)
            gif.save(os.path.join('gif_frames',f'gif{i}.png'))
            self.gif_frames.append(os.path.join('gif_frames',f'gif{i}.png'))

        for images in self.gif_frames:
            im = Image.open(images)
            im = im.resize((500,500),Image.ANTIALIAS)
            im = ImageTk.PhotoImage(im)
            self.images.append(im)

        self.show_animation(0)

    def show_animation(self,count):
        image = self.images[count]
        self.image_label.configure(image=image)
        count += 1
        if count == len(self.images)-1:
            count = 0

        # Muestra la imagen por 10s
        if int(time.time()-self.start) != 5:
            self.x = self.root.after(40,self.show_animation,count)
        else:
            self.root.after_cancel(self.x)
            self.first_screen(self.main_frame)

            shutil.rmtree('gif_frames')

            # Muestra la barra
            self.root.wm_overrideredirect(False)


    def first_screen(self,f):
     
        f.pack_forget()
        first = tk.Frame(self.root)
        first.pack(fill="both",expand=True)
        tk.Label(first,text="Bienvenido al GUI de SecureRoom",font="lucida 15 bold").place(x=40,y=20)
      
        # TÍTULO VPN
        tk.Label(first,text="---------------VPN---------------",font="lucida 13 bold").place(x=40,y=60)

        # FUNCIONES VPN
        def conexion_vpn():
            messagebox.showinfo(message="Abriendo SoftEther VPN Client", title="CONEXION")   
            sp.call(['C:/Program Files/SoftEther VPN Client/vpncmgr_x64.exe'])
        def desconexion_vpn():
            messagebox.showinfo(message="Cerrando SoftEther VPN Client", title="DESCONEXION")
            os.system("taskkill /f /im   vpncmgr_x64.exe")

            #exit()


        # BOTONES VPN
        tk.Label(first,text="Para inciar la conexión VPN, por favor pulse:",font="lucida 13 bold").place(x=40,y=90)
        tk.Label(tk.Button(text="Conectarse a la VPN",font="lucida 12 bold", command=conexion_vpn).place(x=80,y=120))

        tk.Label(first,text="Para inciar la desconexión VPN, por favor pulse:",font="lucida 13 bold").place(x=40,y=160)
        tk.Label(tk.Button(text="Desconectarse de la VPN",font="lucida 12 bold", command=desconexion_vpn).place(x=80,y=190))
        
        # TÍTULO ROOM
        tk.Label(first,text="---------------ROOM---------------",font="lucida 13 bold").place(x=40,y=240)

        # FUNCIONES VPN
        def conexion_room():
            messagebox.showinfo(message="Conectando con la Room, por favor espere...", title="CONEXION")
    
            win32api.ShellExecute (0, "open", "Chat.exe", "", "", 0)
            win32api.ShellExecute (0, "open", "Video.exe", "", "", 1)
           
            
           
    

        def desconexion_room():
            messagebox.showinfo(message="Se ha desconectado correctamente", title="DESCONEXION")  

        # BOTONES ROOM
        tk.Label(first,text="Para inciar la sala, por favor pulse:",font="lucida 13 bold").place(x=40,y=270)
        tk.Label(tk.Button(text="Conectarse a la sala",font="lucida 12 bold", command=conexion_room).place(x=80,y=300))

        tk.Label(first,text="Para inciar la desconexión de la sala, por favor pulse:",font="lucida 13 bold").place(x=40,y=340)
        tk.Label(tk.Button(text="Desconectarse de la sala",font="lucida 12 bold", command=desconexion_room).place(x=80,y=370))

Screen()

