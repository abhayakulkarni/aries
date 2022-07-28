import socket
#from unicodedata import name
s = socket.socket()
print('socket created')

s.bind(('localhost', 9999))

s.listen(3)
print('waiting for connections')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("Connected with", addr, name)

    c.send(bytes('welcome to ARIES', 'utf-8'))

    c.close()
    with open('socket data', 'w') as f:
        f.write(name)