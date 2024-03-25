import socket

server_address = ('127.0.0.1', 20202)
message = f'zad13odp;src;60788;dst;2901;data;programming in python is fun'
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    client_socket.sendto(message.encode(), server_address)
    response, _ = client_socket.recvfrom(1024)
    print('Odpowiedź od serwera:', response.decode())
except ConnectionRefusedError:
    print('Błąd połączenia')
finally:
    client_socket.close()
