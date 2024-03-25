import socket

server_address = ('127.0.0.1', 20202)
    
message1 = f'zad15odpA;ver;4;srcip;212.182.24.27;dstip;192.168.0.2;type;6'
message2 = f'zad15odpB;srcport;2900;dstport;47526;data;network programming is fun'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    sock.sendto(message1.encode(), server_address)
    data, server = sock.recvfrom(1024)
    response = data.decode()
    print('Odpowiedź serwera:', response)
except ConnectionRefusedError:
    print('Błąd połączenia')
finally:
    sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
if response == 'TAK':
    try:
        sock.sendto(message2.encode(), server_address)
        data, server = sock.recvfrom(1024)
        response = data.decode()
        print('Odpowiedź serwera:', response)
    except ConnectionRefusedError:
        print('Błąd połączenia')
    finally:
        sock.close()
