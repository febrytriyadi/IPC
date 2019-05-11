import socket
HOST = '192.168.1.12'
PORT = 1024

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(1)
while (1):
	conn, addr = socket.accept()
	reqFile = conn.recv(1024).decode()
	my_file=open(reqFile,'r') 
	while True:
		c = my_file.read(1024)
		if not c:
			break
		conn.send(c.encode())
		#conn.recv(1024)
	conn.close()
	print (reqFile,' telah di unduh oleh client')
socket.close()