import socket
import threading
from cryptography.fernet import Fernet

HOST = 'localhost'
PORT = 5000
BACKLOG = 5

conexoes = []

def tratar_conexao(conexao, endereco):
    # Gera a chave de criptografia para o cliente
    chave_cliente = Fernet.generate_key()
    cipher_suite = Fernet(chave_cliente)

    # Envia a chave criptografada para o cliente
    conexao.send(chave_cliente)

    while True:
        try:
            mensagem_cifrada = conexao.recv(1024)
            if mensagem_cifrada:
                mensagem = cipher_suite.decrypt(mensagem_cifrada)

                for conn in conexoes:
                    if conn != conexao:
                        conn.send(mensagem_cifrada)

                print('Mensagem recebida cifrada:', mensagem_cifrada)
                print('Mensagem recebida:', mensagem.decode())
            else:
                conexoes.remove(conexao)
                conexao.close()
                print(f'{endereco} desconectado. Total de conexões: {len(conexoes)}')
                break
        except Exception as e:
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
