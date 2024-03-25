import socket

HOST = '127.0.0.1'
PORT = 10101

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Serwer nasłuchuje na {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Połączono z klientem {client_address}")
    message = client_socket.recv(1024).decode()
    print(f"Otrzymano wiadomość od klienta: {message}")

    if message:
        client_socket.sendall(message.encode())
        print('Odesłano dane do klienta:', message)

    client_socket.close()