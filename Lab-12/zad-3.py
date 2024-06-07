import socket
import threading
import random

class ClientThread(threading.Thread):
    def __init__(self, connection):
        threading.Thread.__init__(self)
        self.connection = connection
        self.number_to_guess = random.randint(1, 100)

    def run(self):
        print('Wylosowana liczba do zgadniecia:', self.number_to_guess)
        guessed = False
        while True:
            message = self.connection.recv(1024).decode()
            if not message:
                print('Odłączono klienta ', self.connection.getpeername())
                break
            try:
                guess = int(message)
                if guess < self.number_to_guess:
                    response = 'Za mało'
                elif guess > self.number_to_guess:
                    response = 'Za dużo'
                else:
                    response = 'Zgadłeś!'
                    guessed = True
                self.connection.sendall(response.encode())
            except ValueError:
                self.connection.sendall('To nie jest liczba'.encode())
            print('Odebrana wiadomość:', message)
            if guessed:
                print('Klient zgadł liczbę ', self.number_to_guess)
                print('Odłączono klienta ', self.connection.getpeername())
                break

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