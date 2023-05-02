import socket
import threading

# Define as configurações do cliente
HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024

# Define as mensagens a serem enviadas para o servidor
messages = ['Hello World!!!', 'DCC602 - SISTEMAS DISTRIBUIDOS ', 'Alan Turing']

# Função que envia uma requisição ao servidor com uma mensagem
def send_request(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    client_socket.sendall(message.encode())
    data = client_socket.recv(BUFFER_SIZE)
    client_socket.close()
    print(f'Resposta do servidor para a mensagem "{message}": {data.decode()}')

# Cria as threads para enviar as requisições ao servidor
threads = []
for message in messages:
    thread = threading.Thread(target=send_request, args=(message,))
    threads.append(thread)
    thread.start()

# Espera todas as threads terminarem antes de encerrar o programa
for thread in threads:
    thread.join()
