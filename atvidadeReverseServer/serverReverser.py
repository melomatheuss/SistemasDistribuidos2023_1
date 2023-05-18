'''
MATHEUS DE SOUZA MELO
2019007565
ATIVIDADE MULTITHREADING

'''

import socket
import threading
import time

print_lock = threading.Lock()

def handle_connection(c):
    """
    Função que trata a conexão com um cliente.

    Args:
        c (socket): O socket da conexão com o cliente.
    """
    while True:
        data = c.recv(1024)  # Recebe os dados enviados pelo cliente
        if not data:
            break

        # Simula um processamento intensivo na CPU
        start_time = time.time()
        while time.time() - start_time < 10:  # Processamento por 10 segundos
            pass

        data = data[::-1]  # Inverte os dados recebidos
        c.send(data)  # Envia os dados de volta ao cliente

    c.close()  # Fecha a conexão com o cliente

def main():
    host = "localhost"
    port = 5000
    backlog = 5

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))  # Associa o socket a um endereço e porta
        print("Socket vinculado à porta", port)

        s.listen(backlog)  # Habilita o socket para receber conexões
        print("Socket está escutando")

        while True:
            c, addr = s.accept()  # Aceita uma conexão de um cliente
            print('Conectado em:', addr[0], ':', addr[1])

            thread = threading.Thread(target=handle_connection, args=(c,))
            thread.start()  # Inicia uma thread para tratar a conexão

if __name__ == '__main__':
    main()


