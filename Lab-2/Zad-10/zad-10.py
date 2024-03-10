import socket

server_address = ('127.0.0.1', 2907)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    hostname = input("Podaj hostname: ")
    client_socket.sendto(hostname.encode(), server_address)
    ip_address, _ = client_socket.recvfrom(1024)

    print(f'Otrzymany adres IP: {ip_address.decode()}')
except ConnectionRefusedError:
    print('Błąd połączenia')
finally:
    client_socket.close()