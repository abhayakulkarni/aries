import socket
import numpy as np
import encodings


HOST = '127.0.0.1'
PORT = 65432


def random_data():
	x1 = np.random.randint(0,55, None)
	y1 = np.random.randint(0,45, None)
	my_sensor = "{},{}".format(x1,y1) 
	return my_sensor



def my_server():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		print("Server started waiting for client to connect")
		s.bind((HOST, PORT))
		s.listen(S)
		conn, addr = s.accept()
		
		with conn:
			print('connected by', addr)
			while True:
				data = conn.recv(1024).decode('utf-8')

				if str(data) == "data":
					print("Ok sending data")
					my_data = random_data()

					x_encoded_data = my_data.encode('utf-8')
					conn.sendall(x_encoded_data)
				elif str(data) == "Quit":
					print("shutting down server")
					break

				if not data:
					break
				else:
					pass

if __name__ == 'main':
	while 1:
		myserver()
