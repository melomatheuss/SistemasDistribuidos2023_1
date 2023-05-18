import socket
import threading

print_lock = threading.Lock()

def threaded(c):
    while True:
        data = c.recv(1024)
        if not data:
            print('Conexão finalizada. Obrigado e até logo!')
            break

        data = data[::-1]

        c.send(data)

    c.close()

def Main():
    host = ""
    port = 5000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("Socket vinculado à porta", port)

    s.listen(5)
    print("Socket está escutando")

    while True:
        c, addr = s.accept()

        print_lock.acquire()
        print('Conectado em:', addr[0], ':', addr[1])

        thread = threading.Thread(target=threaded, args=(c,))
        thread.start()

    s.close()

if __name__ == '__main__':
    Main()

