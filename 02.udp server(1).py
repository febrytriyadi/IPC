import socket
 
IP = "192.168.1.12"
PORT = 50000
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

while True:
    data, address = sock.recvfrom(1024)
    print ("received :", data.decode())