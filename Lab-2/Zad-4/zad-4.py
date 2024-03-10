import socket

server_address = ('127.0.0.1', 2901)
message = 'Hello, server!'
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.sendto(message.encode(), server_address)
    data, server = sock.recvfrom(1024)
    response = data.decode()
    print('Odpowiedź serwera:', response)
except ConnectionRefusedError:
    print('Błąd połączenia')
finally:
    sock.close()