import socket
import os

HOST = '192.168.1.12'    
PORT = 1026
uploadDir = "tmp"
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(1)
while (1):
	conn, addr = socket.accept()
	with open(os.path.join(uploadDir, "hasil_upload.txt"), 'w+') as file_to_write:
	    while True:
	        data = conn.recv(1024)
	        if not data:
	            break
	        file_to_write.write(str(data))
	    file_to_write.close()
	    print('file berhasil di simpan')
	conn.close()
socket.close()