import socket
 
IP = "192.168.1.12"
PORT = 50000
print ("Destination IP:", IP)
print ("Destination port:", PORT)
 
for i in range (10):
    data = "Message: "+ str(i+1)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(data.encode(), (IP, PORT))