import socket
import time

HOST = '127.0.0.1'
PORT1 = 1234
PORT2 = 5678
TEST_RANGE = 1000

def tcp_client():
    print('Klient TCP')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((HOST, PORT1))

        for i in range(TEST_RANGE):
            data = str(i)
            sock.sendall(data.encode())
            print(f'Wysłano: {data}')
            sock.recv(1024)
            print(f'Odpowiedź: {data}')
    except ConnectionRefusedError:
        print('Błąd połączenia')
    finally:
        sock.close()
        
def udp_client():
    print('Klient UDP')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        for i in range(TEST_RANGE):
            data = str(i)
            sock.sendto(data.encode(), (HOST, PORT2))
            print(f'Wysłano: {data}')
            sock.recv(1024)
            print(f'Odpowiedź: {data}')
    except ConnectionRefusedError:
        print('Błąd połączenia')
    finally:
        sock.close()
        
if __name__ == '__main__':
    tcp_client()
    time.sleep(1)
    udp_client()