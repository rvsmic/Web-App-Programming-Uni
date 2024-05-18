import socket
import hashlib
import base64

def handle_websocket(client_socket):
    request = client_socket.recv(1024).decode()
    headers = request.split('\r\n')

    if 'Upgrade: websocket' not in headers:
        response = "HTTP/1.1 400 Bad Request\r\n\r\n"
        client_socket.send(response.encode())
        return

    response = "HTTP/1.1 101 Switching Protocols\r\n"
    response += "Upgrade: websocket\r\n"
    response += "Connection: Upgrade\r\n"

    key = None
    for header in headers:
        if 'Sec-WebSocket-Key' in header:
            key = header.split(': ')[1]
            break

    if key:
        accept_key = base64.b64encode(hashlib.sha1((key + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11').encode()).digest()).decode()
        response += "Sec-WebSocket-Accept: " + accept_key + "\r\n"

    response += "\r\n"
    client_socket.send(response.encode())

def main():
    host = "127.0.0.1"
    port = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Serwer WebSocket nasłuchuje na adresie", host, "i porcie", port)

    while True:
        client_socket, client_address = server_socket.accept()
        print("Połączono z klientem:", client_address)

        handle_websocket(client_socket)

        client_socket.close()

if __name__ == "__main__":
    main()