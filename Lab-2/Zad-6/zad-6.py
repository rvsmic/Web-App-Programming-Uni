import socket

server_address = ('127.0.0.1', 2902)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    num1 = int(input("Podaj pierwszą liczbę: "))
    operator = input("Podaj operator (+, -, *, /): ")
    num2 = int(input("Podaj drugą liczbę: "))

    client_socket.sendto(str(num1).encode(), server_address)
    client_socket.sendto(operator.encode(), server_address)
    client_socket.sendto(str(num2).encode(), server_address)

    response, _ = client_socket.recvfrom(1024)
    print("Odpowiedź od serwera:", response.decode())
except ConnectionRefusedError:
    print('Błąd połączenia')
finally:
    client_socket.close()