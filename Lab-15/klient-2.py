import socket

if __name__ == "__main__":
    server_address = ('127.0.0.1', 6666)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    print('Połączono z serwerem')
    print('Dostępne komendy: \n - FULL - wszystkie dane pogodowe\n - TEMP - dane o temperaturze\n - HUM - dane o wilgotności\n - PRES - dane o ciśnieniu\n - WIND - dane o wietrze\n - EXIT - zakończenie połączenia\n')
    try:
        while True:
            command = input("Wpisz komendę: ")
            client_socket.sendall(command.encode())

            response = client_socket.recv(1024)
            print('Otrzymano:', response.decode())
            
            if command == 'EXIT':
                break
    finally:
        client_socket.close()
