import socket 


#HOST = '172.29.55.198'  # The server's hostname or IP address
#PORT = 65435      # The port used by the server


c = socket.socket()

c.connect(('172.29.55.198',9999))

name = input("Enter your name")
c.send(bytes(name,'utf-8'))

print(c.recv(1024).decode())