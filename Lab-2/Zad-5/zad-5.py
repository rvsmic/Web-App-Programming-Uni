import socket

server_address = ('127.0.0.1', 2901)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Wpisz wiadomość: ")
    if message == "exit":
        break
    client_socket.sendto(message.encode(), server_address)
    data, _ = client_socket.recvfrom(1024)
    response = data.decode()
    print("Odpowiedź serwera:", response)

client_socket.close()