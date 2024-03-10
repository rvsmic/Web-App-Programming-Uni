import socket

# We wszystkich zadaniach z tego laboratorium serwer i klient będą działać na tym samym komputerze - zmieniłem adres na lokalny
server_address = ('127.0.0.1', 2900)
message = 'Hello, server!'
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(server_address)
    client_socket.sendall(message.encode())
    response = client_socket.recv(1024).decode()
    print('Odpowiedź od serwera:', response)
except ConnectionRefusedError:
    print('Błąd połączenia')
finally:
    client_socket.close()