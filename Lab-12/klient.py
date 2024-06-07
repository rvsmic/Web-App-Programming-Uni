import socket

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def run(self):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((self.ip, self.port))
            print('Połączono z serwerem')

            while True:
                message = input('Wpisz wiadomość: ')
                client_socket.sendall(message.encode())
                response = client_socket.recv(1024).decode()
                print('Odebrana wiadomość:', response)
                if response == 'Zgadłeś!':
                    client_socket.close()
                    break

        except socket.error as e:
            print('Socket error:', e)

if __name__ == '__main__':
    c = Client('127.0.0.1', 6666)
    c.run()