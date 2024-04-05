import socket

server_address = ('127.0.0.1', 2912)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(server_address)
except ConnectionRefusedError:
    print('Błąd połączenia')
    exit()

message = ''
print("Aby zakończyć wpisz 'exit'")

while message != 'exit':
    message = input("Podaj liczbę do wysłania: ")
    client_socket.send(str(message).encode())
    response = client_socket.recv(1024).decode()
    print(response)
    if response == "Udało ci sie odgadnąć liczbę!":
        break

client_socket.close()