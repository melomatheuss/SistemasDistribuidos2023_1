'''
MATHEUS DE SOUZA MELO
2019007565
ATIVIDADE MULTITHREADING

'''

import socket
import threading

HOST = 'localhost'  # Endereço IP do servidor
PORT = 5000  # Porta de conexão com o servidor
BUFFER_SIZE = 1024  # Tamanho do buffer para recebimento de dados

messages = ['Hello World!!!', 'DCC602 - SISTEMAS DISTRIBUIDOS', 'Alan Turing',
            'Hello World!!!', 'DCC602 - SISTEMAS DISTRIBUIDOS', 'Alan Turing',
            'Hello World!!!', 'DCC602 - SISTEMAS DISTRIBUIDOS', 'Alan Turing',
            'Hello World!!!', 'DCC602 - SISTEMAS DISTRIBUIDOS', 'Alan Turing',
            'Hello World!!!', 'DCC602 - SISTEMAS DISTRIBUIDOS', 'Alan Turing']
# Lista de mensagens a serem enviadas para o servidor

def send_request(message):
    """
    Função que envia uma requisição ao servidor com uma mensagem e imprime a resposta.

    Args:
        message (str): A mensagem a ser enviada para o servidor.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((HOST, PORT))  # Conecta ao servidor
            client_socket.sendall(message.encode())  # Envia a mensagem codificada
            data = client_socket.recv(BUFFER_SIZE)  # Recebe a resposta do servidor
            print(f'Resposta do servidor para a mensagem "{message}": {data.decode()}')
        except Exception as e:
            print(f'Ocorreu uma exceção durante o processamento da mensagem "{message}": {str(e)}')

def attack():
    """
    Função que realiza o ataque ao servidor, enviando requisições com as mensagens.
    """
    while True:
        for message in messages:
            thread = threading.Thread(target=send_request, args=(message,))
            thread.start()

num_threads = 300  # Número de threads para enviar as requisições
threads = []

for _ in range(num_threads):
    thread = threading.Thread(target=attack)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
