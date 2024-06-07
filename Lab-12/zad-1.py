import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, connection):
        threading.Thread.__init__(self)
        self.connection = connection

    def run(self):
        while True:
            message = self.connection.recv(1024).decode()
            if not message:
                print('Odłączono klienta ', self.connection.getpeername())
                break
            print('Odebrana wiadomość:', message)
            self.connection.sendall(message.encode())

class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def run(self):
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((self.ip, self.port))
            server_socket.listen(1)
            print(f'Serwer nasłuchuje na adresie {self.ip} i porcie {self.port}')

            while True:
                client_socket, client_address = server_socket.accept()
                print('Połączono z ', client_address)

                c = ClientThread(client_socket)
                c.start()

        except socket.error as e:
            print('Socket error:', e)

if __name__ == '__main__':
    s = Server('127.0.0.1', 6666)
    s.run()