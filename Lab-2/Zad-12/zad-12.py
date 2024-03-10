import socket

server_address = ('127.0.0.1', 2908)
message = 'Hello, server!'
if len(message) < 20:
    message = message.ljust(20)
elif len(message) > 20:
    message = message[:20]
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect(server_address)
    total_sent = 0
    while total_sent < len(message):
        sent = client_socket.send(message[total_sent:].encode())
        if sent == 0:
            raise RuntimeError("Socket connection broken")
        total_sent += sent
    
    response = ''
    while len(response) < 1024:
        chunk = client_socket.recv(1024 - len(response)).decode()
        if chunk == '':
            raise RuntimeError("Socket connection broken")
        response += chunk
    
    print('Odpowiedź od serwera:', response)
except ConnectionRefusedError:
    print('Błąd połączenia')
finally:
    client_socket.close()