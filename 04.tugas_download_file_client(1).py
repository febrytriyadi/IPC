import socket
import os

HOST = '192.168.1.12'    
PORT = 1024
downloadDir = "tmp"


filename = "file_didownload.txt"
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect((HOST, PORT))
socket1.send(filename.encode())
with open(os.path.join(downloadDir, "hasil_download.txt"), 'w+') as file_to_write:
    while True:
        data = socket1.recv(1024).decode()
        if not data:
            break
        file_to_write.write(data)
    file_to_write.close()
    print("file downloaded")
socket1.close()