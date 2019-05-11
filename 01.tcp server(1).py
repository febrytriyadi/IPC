import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.17', 12345))
s.listen(2)
print('server hidup')
conn, addr = s.accept()
while 1:
    data = conn.recv(1024).decode()
    print(addr, ' -> server : ',data)
    conn.sendall(data.encode())
    print('server -> ',addr,' : ',data)
conn.close()