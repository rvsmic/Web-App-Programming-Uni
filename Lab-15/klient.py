import socket
from time import sleep

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def run(self):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((self.ip, self.port))
            print('Połączono z serwerem')
            
            message = input('Wpisz wiadomość: ')

            while True:
                client_socket.sendall(message.encode())
                response = client_socket.recv(1024).decode()
                print('Odebrana wiadomość:', response)
                sleep(2)

        except socket.error as e:
            print('Socket error:', e)

if __name__ == '__main__':
    c = Client('127.0.0.1', 6666)
    c.run()