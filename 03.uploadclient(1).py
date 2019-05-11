import socket
HOST = '192.168.1.12'
PORT = 1026

filename = "file_diupload.txt"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
#s.send(open(filename,'r').read().encode())
my_file=open(filename,'rb')
while True:
	c = my_file.read(1024)
	if not c:
		break
	s.send(c)
print("File sended")
s.close()
