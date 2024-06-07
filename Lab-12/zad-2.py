import socket
import threading
from datetime import datetime

class ClientThread(threading.Thread):
    def __init__(self, connection):
        threading.Thread.__init__(self)
        self.connection = connection

    def run(self):
        while True:
            message = self.connection.recv(1024).decode()
            client_address = self.connection.getpeername()
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if not message:
                print('Odłączono klienta ', client_address)
                with open('server_log.txt', 'a') as log_file:
                    log_message = f'{current_time} - Odłączono klienta: {client_address}\n'
                    log_file.write(log_message)
                break
            print('Odebrana wiadomość:', message)
            with open('server_log.txt', 'a') as log_file:
                log_message = f'{current_time} - Odebrano wiadomość klienta {client_address}: {message}\n'
                log_file.write(log_message)
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

                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                with open('server_log.txt', 'a') as log_file:
                    log_message = f'{current_time} - Nowy klient: {client_address}\n'
                    log_file.write(log_message)

                c = ClientThread(client_socket)
                c.start()

        except socket.error as e:
            print('Socket error:', e)

if __name__ == '__main__':
    s = Server('127.0.0.1', 6666)
    s.run()