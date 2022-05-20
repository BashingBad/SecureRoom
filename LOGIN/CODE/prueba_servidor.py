import socket
import threading


PORT = 3000
SERVER = '127.0.0.1'


ADDRESS = (SERVER, PORT)

FORMAT = "utf-8"


clients, names = [], []


server = socket.socket(socket.AF_INET,
					socket.SOCK_STREAM)


server.bind(ADDRESS)


def startChat():

	print("Servidor corriendo en la IP " + SERVER)
	
	# listening for connections
	server.listen()
	
	while True:
	
		conn, addr = server.accept()
		#conn.send("Nombre".encode(FORMAT))
		

		name = conn.recv(1024).decode(FORMAT)
		print (name)
		names.append(name)
		clients.append(conn)
		
		#print(f"Name is :{name}")
		
		
		broadcastMessage(f"{name} se ha unido al chat!".encode(FORMAT))
		
		conn.send('Conexión satisfactoria!'.encode(FORMAT))
		
	
		thread = threading.Thread(target = handle,
		args = (conn, addr))
		thread.start()
		
		print(f"Conexiones activas {threading.activeCount()-1}")


def handle(conn, addr):

	print(f"Nueva conexión {addr}")
	connected = True
	
	while connected:
		message = conn.recv(1024)
		
		broadcastMessage(message)
	
	conn.close()


def broadcastMessage(message):
	for client in clients:
		client.send(message)


startChat()



