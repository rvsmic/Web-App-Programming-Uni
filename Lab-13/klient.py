import socket
import os

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = None
        
    def send_file(self, filename):
        self.socket.sendall(b'UPLOAD')
        response = self.socket.recv(1024).decode()
        if response == 'OK':
            print('Przesyłam nazwę pliku...')
            self.socket.sendall(filename.encode())
            print('Zakończyłem przesyłać nazwę pliku...')
            filesize = str(os.stat(filename).st_size)
            print('Przesyłam rozmiar pliku...')
            self.socket.sendall(filesize.encode())
            print('Zakończyłem przesyłać rozmiar pliku...')
            try:
                with open(filename, 'rb') as file:
                    print('Przesyłam plik...')
                    for data in file:
                        self.socket.sendall(data)
                    print('Zakończyłem przesyłać plik...')
            except FileNotFoundError:
                print('Nie odnaleziono pliku:', filename)
                return
            response = self.socket.recv(1024).decode()
            print(f'Odpowiedź serwera: {response}')
        else:
            print(f'Odpowiedź serwera: {response}')

    def run(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.ip, self.port))
            print('Połączono z serwerem')
            
            while True:
                filename = input('Wpisz nazwe pliku do wysłania: ')
                self.send_file(filename)
        except socket.error as e:
            print('Błąd połączenia:', e)

c = Client('127.0.0.1', 1234)
c.run()