import socket

s = socket.socket()

s.connect(("192.168.1.17",12345))
a=input("kirim ke server : ")
while a!='':
	s.send((a).encode())
	print("server : ",s.recv(1024).decode())
	a=input("kirim ke server : ")
s.close()