import socket
import threading
import time


HOST = '192.168.0.111'
PORT = 65432



def process_data_from_server(x):
	x1,y1 = x.split(",")
	return x1,y1

def my_client():
	threading.Timer(11, my_client).start()
	
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		
		my = input("Enter Command")

		my_inp =  my.encode('utf-8')
		s.sendall(my_inp)
		data = s.recv(1024).decode('utf-8')
		x_temparature, y_humidity = process_data_from_server(data)

		print("Temparature ()", format(x_temparature))
		print("Humidity ()", format(y_humidity))

		s.close()
		time.sleep(5)

if __name__ == "__main__"
	while 1:
		my_client()
