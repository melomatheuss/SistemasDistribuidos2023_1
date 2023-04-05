import socket
import threading
from cryptography.fernet import Fernet

HOST = ''
PORT = 5000
BACKLOG = 5


key = Fernet.generate_key()


cipher_suite = Fernet(key)


conexoes = []

def tratar_conexao(conexao, endereco):

    conexao.send(key)

    while True:
        try:
            mensagem_cifrada = conexao.recv(1024)
            if mensagem_cifrada:
                mensagem = cipher_suite.decrypt(mensagem_cifrada)

                for conn in conexoes:
                    if conn != conexao:
                        conn.send(mensagem_cifrada)
            else:
                conexoes.remove(conexao)
                conexao.close()
                print(f'{endereco} desconectado. Total de conexões: {len(conexoes)}')
                break
        except Exception as e:
            # Se ocorrer um erro na conexão, remove a conexão da lista e encerra o loop
            conexoes.remove(conexao)
            conexao.close()
            print(f'{endereco} desconectado. Total de conexões: {len(conexoes)}')
            break

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen(BACKLOG)

print(f'Servidor iniciado. Aguardando conexão na porta {PORT}')

while True:
    conexao, endereco = servidor.accept()
    print(f'{endereco} conectado. Total de conexões: {len(conexoes) + 1}')

    conexoes.append(conexao)

    thread = threading.Thread(target=tratar_conexao, args=(conexao, endereco))
    thread.start()

servidor.close()

print('Servidor encerrado.')
