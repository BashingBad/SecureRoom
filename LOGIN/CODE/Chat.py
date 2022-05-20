import socket
import threading
import tkinter as tk
from tkinter import *




PORT = 2000
SERVER = '10.147.18.237'

ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"


client = socket.socket(socket.AF_INET,
					socket.SOCK_STREAM)
client.connect(ADDRESS)



class GUI:
	
	def __init__(self):
	
		self.Window = tk.Tk()
		self.Window.withdraw()
		self.Window.iconbitmap(default="icono.ico")

		self.login = Toplevel()
		self.login.title("Login")
        
		self.login.resizable(width = False, height = False)
		self.login.configure(width = 400, height = 300)
		# create a Label
		self.pls = Label(self.login,
					text = "Ingrese su nombre de usuario",
					justify = CENTER,
					font = "Helvetica 14 bold")
		
		self.pls.place(relheight = 0.15,
					relx = 0.2,
					rely = 0.07)
		# create a Label
		self.labelName = Label(self.login,
							text = "Nombre: ",
							font = "Helvetica 12 bold")
		
		self.labelName.place(relheight = 0.2,
							relx = 0.1,
							rely = 0.2)
		
		# create a entry box for
		# tyoing the message
		self.entryName = Entry(self.login,
							font = "Helvetica 14")
		
		self.entryName.place(relwidth = 0.4,
							relheight = 0.12,
							relx = 0.35,
							rely = 0.2)
		
		# set the focus of the cursor
		self.entryName.focus()
		
		# create a Continue Button
		# along with action
		self.go = Button(self.login,
						text = "Siguiente",
						font = "Helvetica 14 bold",
						command = lambda: self.goAhead(self.entryName.get()))
		
		self.go.place(relx = 0.4,
					rely = 0.55)
		self.Window.mainloop()

	def goAhead(self, name):
		self.login.destroy()
		self.layout(name)
		
		# the thread to receive messages
		rcv = threading.Thread(target=self.receive)
		rcv.start()

	# The main layout of the chat
	def layout(self,name):
	
		self.name = name
		# to show chat window
		self.Window.deiconify()
		self.Window.title("Chat")
		self.Window.resizable(width = False,
							height = False)
		self.Window.configure(width = 470,
							height = 550,
							bg = "#F1A11E")
		self.labelHead = Label(self.Window,
							bg = "#F1A11E",
							fg = "#000000",
							text = self.name ,
							font = "Helvetica 13 bold",
							pady = 5)
		
		self.labelHead.place(relwidth = 1)
		self.line = Label(self.Window,
						width = 450,
						bg = "#000000")
		
		self.line.place(relwidth = 1,
						rely = 0.07,
						relheight = 0.012)
		
		self.textCons = Text(self.Window,
							width = 20,
							height = 2,
							bg = "#F1A11E",
							fg = "#000000",
							font = "Helvetica 14",
							padx = 5,
							pady = 5)
		
		self.textCons.place(relheight = 0.745,
							relwidth = 1,
							rely = 0.08)
		
		self.labelBottom = Label(self.Window,
								bg = "#F1A11E",
								height = 80)
		
		self.labelBottom.place(relwidth = 1,
							rely = 0.825)
		
		self.entryMsg = Entry(self.labelBottom,
							bg = "#F1A11E",
							fg = "#000000",
							font = "Helvetica 13 bold")
		
		# place the given widget
		# into the gui window
		self.entryMsg.place(relwidth = 0.74,
							relheight = 0.06,
							rely = 0.008,
							relx = 0.011)
		
		self.entryMsg.focus()
		
		# create a Send Button
		self.buttonMsg = Button(self.labelBottom,
								text = "Enviar",
								font = "Helvetica 10 ",
								width = 20,
								bg = "#F1A11E",
								command = lambda : self.sendButton(self.entryMsg.get()))

		self.buttonMsg.place(relx = 0.77,
							rely = 0.008,
							relheight = 0.06,
							relwidth = 0.22)
		
		self.textCons.config(cursor = "arrow")
		
		# create a scroll bar
		scrollbar = Scrollbar(self.textCons)
		
		# place the scroll bar
		# into the gui window
		scrollbar.place(relheight = 1,
						relx = 0.974)
		
		scrollbar.config(command = self.textCons.yview)
		
		self.textCons.config(state = DISABLED)

	# function to basically start the thread for sending messages
	def sendButton(self, msg):
		self.textCons.config(state = DISABLED)
		self.msg=msg
		self.entryMsg.delete(0, END)
		snd= threading.Thread(target = self.sendMessage)
		snd.start()

	# function to receive messages
	def receive(self):
		while True:
			try:
				message = client.recv(1024).decode(FORMAT)
				
				# if the messages from the server is NAME send the client's name
				if message == 'NAME':
					client.send(self.name.encode(FORMAT))
				else:
					# insert messages to text box
					self.textCons.config(state = NORMAL)
					self.textCons.insert(END,
										message+"\n\n")
					
					self.textCons.config(state = DISABLED)
					self.textCons.see(END)
			except:
				# an error will be printed on the command line or console if there's an error
				print("Ha ocurrido un error!")
				client.close()
				break
		
	# function to send messages
	def sendMessage(self):
		self.textCons.config(state=DISABLED)
		while True:
			message = (f"{self.name}: {self.msg}")
			client.send(message.encode(FORMAT))
		
			break

# create a GUI class object
GUI()
