import socket

from _thread import *
import threading

print_lock = threading.Lock()

def threaded(c):
	while True:

		data = c.recv(1024)
		if not data:
			print('Conecao finaizada vlw flw')
			
			print_lock.release()
			break

		data = data[::-1]

		c.send(data)

	c.close()


def Main():
	host = ""

	port = 5000
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	print("socket vinculado a porta", port)

	s.listen(5)
	print("socket esta escutando")

	while True:

		c, addr = s.accept()

		print_lock.acquire()
		print('conctado em :', addr[0], ':', addr[1])

		start_new_thread(threaded, (c,))
	s.close()

if __name__ == '__main__':
	Main()
