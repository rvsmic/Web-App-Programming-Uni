import socket
import time

HOST = '127.0.0.1'
PORT1 = 1234
PORT2 = 5678
TEST_RANGE = 1000

def tcp_server():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((HOST, PORT1))
    tcp_socket.listen(1)
    print("Uruchomiono serwer TCP")
    conn, addr = tcp_socket.accept()
    print("Nawiązano połączenie TCP z: ", addr)

    start_time = None
    while True:
        data = conn.recv(1024)
        if not start_time:
            start_time = time.time()
        if not data:
            break

        response = "Serwer TCP otrzymał: " + data.decode()
        print(response)
        conn.sendall(response.encode())
        if data.decode() == str(TEST_RANGE - 1):
            tcp_execution_time = time.time() - start_time
            break
    tcp_socket.close()
    return tcp_execution_time

def udp_server():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((HOST, PORT2))
    print("Uruchomiono serwer UDP")

    start_time = None
    while True:
        data, addr = udp_socket.recvfrom(1024)
        if not start_time:
            start_time = time.time()
        if not data:
            break
        
        response = "Serwer UDP otrzymał: " + data.decode()
        print(response)
        udp_socket.sendto(response.encode(), addr)
        if data.decode() == str(TEST_RANGE - 1):
            udp_execution_time = time.time() - start_time
            break
    udp_socket.close()
    return udp_execution_time

if __name__ == '__main__':
    tcp_execution_time = tcp_server()
    udp_execution_time = udp_server()

    print("Czas wykonania serwera TCP:", tcp_execution_time)
    print("Czas wykonania serwera UDP:", udp_execution_time)