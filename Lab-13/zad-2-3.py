import socket
import os

# serwer pod adresem 212.182.24.27 nie działa więc używam lokalnego

class FileServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.filename = "obrazek.png"
        self.filesize = str(os.stat(self.filename).st_size)

    def send_file(self, connection):
        print('Przesyłam odpowiedź...')
        connection.sendall(f'SIZE {self.filesize} NAME {self.filename.encode()}'.encode())
        print('Zakończyłem przesyłać odpowiedź...')
        try:
            with open(self.filename, 'rb') as file:
                print('Przesyłam plik...')
                for data in file:
                    connection.sendall(data)
                print('Zakończyłem przesyłać plik...')
        except FileNotFoundError:
            print('Nie odnaleziono pliku:', self.filename)
            return

    def handle_client(self, connection):
        while True:
            command = connection.recv(1024).decode()
            if command == 'GET_IMAGE':
                print('Odebrano żądanie GET_IMAGE')
                self.send_file(connection)
                print('Zakończono obsługę klienta')
            else:
                print('Nieznana komenda')
                connection.sendall(b'ERROR')
                break

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        print(f'Serwer nasłuchuje na {self.host}:{self.port}...')

        while True:
            connection, address = self.socket.accept()
            print(f'Połączono z klientem: {address[0]}:{address[1]}')
            self.handle_client(connection)
            connection.close()
            print(f'Odłączono klienta: {address[0]}:{address[1]}')

server = FileServer('127.0.0.1', 1234)
server.run()
