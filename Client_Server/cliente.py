'''
ATIVIDADE 1 MATHEUS DE SOUZA MELO
2019007565
ATIVIDADE REVISADA, RESOVENDO O PROBLEMA CITADO PELO PREFESSOR.
'''

import socket
import threading
from cryptography.fernet import Fernet

HOST = 'localhost'
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

# Recebe a chave criptografada do servidor
chave_criptografada = cliente.recv(1024)
print(f'Chave recebida do servidor: {chave_criptografada}')

# Inicializa o objeto Fernet com a chave recebida do servidor
cipher_suite = Fernet(chave_criptografada)

def receber_mensagem():
    while True:
        mensagem_cifrada = cliente.recv(1024)
        if mensagem_cifrada:
            mensagem = cipher_suite.decrypt(mensagem_cifrada)
            print('Mensagem recebida cifrada:', mensagem_cifrada)
            print('Mensagem recebida:', mensagem.decode())

def enviar_mensagem():
    while True:
        mensagem = input()
        mensagem_cifrada = cipher_suite.encrypt(mensagem.encode())
        cliente.send(mensagem_cifrada)

thread_receber = threading.Thread(target=receber_mensagem)
thread_receber.start()

thread_enviar = threading.Thread(target=enviar_mensagem)
thread_enviar.start()
