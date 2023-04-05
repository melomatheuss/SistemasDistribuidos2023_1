import socket
from cryptography.fernet import Fernet
import threading

HOST = 'localhost'
PORT = 5000

# Criando o objeto de cifra com a chave pública recebida do servidor
key = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
key.connect((HOST, PORT))
cipher_key = key.recv(1024)
cipher_suite = Fernet(cipher_key)

def enviar_mensagem():
    while True:
        mensagem = input()
        mensagem_cifrada = cipher_suite.encrypt(mensagem.encode())
        cliente.send(mensagem_cifrada)

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

thread_enviar_mensagem = threading.Thread(target=enviar_mensagem)
thread_enviar_mensagem.start()

while True:
    mensagem_cifrada = cliente.recv(1024)

    if mensagem_cifrada:
        # Descriptografando a mensagem recebida
        mensagem = cipher_suite.decrypt(mensagem_cifrada)
        print(mensagem.decode())
    else:
        # Se a mensagem for vazia, encerra o loop
        cliente.close()
        print('Conexão encerrada.')
        break
