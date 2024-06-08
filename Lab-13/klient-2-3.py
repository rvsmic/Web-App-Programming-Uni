import socket
import os

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = None
        
    def receive_file(self, filename, filesize):
        read_bytes = 0
        bytes_to_read = 0
        with open('klient-' + filename, 'ab') as file:
            while read_bytes < filesize:
                bytes_to_read = 1024
                if read_bytes >= filesize:
                    bytes_to_read = filesize % 1024
                read_bytes += bytes_to_read
                data = self.socket.recv(bytes_to_read)
                file.write(data)

    def run(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.ip, self.port))
            print('Połączono z serwerem')
            
            while True:
                command = input('Wpisz komendę (GET_IMAGE): ')
                self.socket.sendall(command.encode())
                response = self.socket.recv(1024).decode()
                print('Odebrana odpowiedź:', response)
                if not response.startswith('SIZE'):
                    print('Błąd odpowiedzi serwera')
                    continue
                try:
                    filesize = int(response.split(' ')[1])
                except ValueError:
                    print('Nieprawidłowy rozmiar pliku')
                    continue
                print('Odebrano rozmiar pliku:', filesize)
                filename = response.split(' ')[3].split("'")[1].split("'")[0]
                print('Odebrano nazwę pliku:', filename)
                print('Czekam na plik...')
                self.receive_file(filename, filesize)
                print(f'Odebrano plik i zapisano pod nazwą klient-{filename}')
        except socket.error as e:
            print('Błąd połączenia:', e)

c = Client('127.0.0.1', 1234)
c.run()