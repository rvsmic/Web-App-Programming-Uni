import socket

server_address = ('127.0.0.1', 2900)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(server_address)
    print('Połączono z serwerem.')
    while True:
        message = input('Wpisz wiadomość: ')
        client_socket.sendall(message.encode())
        response = client_socket.recv(1024).decode()
        print('Odpowiedź serwera:', response)
except ConnectionRefusedError:
    print('Błąd połączenia')
finally:
    client_socket.close()