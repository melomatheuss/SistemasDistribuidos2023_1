import socket
import threading

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024

messages = ['Hello World!!!', 'DCC602 - SISTEMAS DISTRIBUIDOS', 'Alan Turing']

def send_request(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((HOST, PORT))
            client_socket.sendall(message.encode())
            data = client_socket.recv(BUFFER_SIZE)
            print(f'Resposta do servidor para a mensagem "{message}": {data.decode()}')
        except Exception as e:
            print(f'Ocorreu uma exceção durante o processamento da mensagem "{message}": {str(e)}')

def attack():
    while True:
        for message in messages:
            thread = threading.Thread(target=send_request, args=(message,))
            thread.start()

num_threads = 10
threads = []

for _ in range(num_threads):
    thread = threading.Thread(target=attack)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
