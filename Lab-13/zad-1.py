import socket

class FileServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None

    def receive_file(self, connection, filename, filesize):
        read_bytes = 0
        bytes_to_read = 0
        with open('odebrany-' + filename, 'ab') as file:
            while read_bytes < filesize:
                bytes_to_read = 1024
                if read_bytes >= filesize:
                    bytes_to_read = filesize % 1024
                read_bytes += bytes_to_read
                data = connection.recv(bytes_to_read)
                file.write(data)

    def handle_client(self, connection):
        command = connection.recv(1024).decode()
        if command == 'UPLOAD':
            connection.sendall(b'OK')
            print('Czekam na nazwę pliku...')
            filename = connection.recv(1024).decode()
            print('Odebrałem nazwę pliku...')
            print('Czekam na rozmiar pliku...')
            try:
                filesize = int(connection.recv(1024).decode())
            except ValueError:
                print('Nieprawidłowy rozmiar pliku')
                connection.sendall('Nieprawidłowy rozmiar pliku'.encode())
                return
            print('Odebrałem rozmiar pliku...')
            print('Czekam na plik...')
            self.receive_file(connection, filename, filesize)
            print(f'Odebrałem plik i zapisałem pod nazwą odebrany-{filename}...')
            connection.sendall(f'Serwer odebrał plik {filename}'.encode())
        else:
            print('Nieznana komenda')
            connection.sendall(b'Nieznana komenda')

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