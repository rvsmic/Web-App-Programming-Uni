import socket
import random

def generate_random_number():
    return random.randint(1, 100)

HOST = '127.0.0.1'
PORT = 2912

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

info_message = "Odgadnij liczbę z zakresu 1-100!"
ok_message = "Udało ci sie odgadnąć liczbę!"
bigger_message = "Nie udało ci się odgadnąć liczby! Odgadywana liczba jest większa!"
smaller_message = "Nie udało ci się odgadnąć liczby! Odgadywana liczba jest mniejsza!"
next_number_message = "Generuje kolejną liczbę do zgadywania..."
ready_message = "Serwer jest gotowy do ponownej gry!"
num_error = "Podana wartość nie jest liczbą!"

print(f"Serwer działa na {HOST}:{PORT}")
random_number = generate_random_number()
print("Liczba do zgadnięcia:", random_number)
client_socket, addr = server_socket.accept()
print(f"Połączono z {addr[0]}:{addr[1]}")

while True:
    try:
        message = client_socket.recv(1024).decode()
    except ConnectionResetError:
        print("Klient zakończył połączenie")
        break
    print(f"Otrzymano od klienta: {message}")
    try:
        number = int(message)
    except ValueError:
        client_socket.send(num_error.encode())
        print(f"Otrzymana wiadomośc nie jest liczbą: {message}")
        continue
    if number == random_number:
        client_socket.send(ok_message.encode())
        print("Udało się odgadnąć liczbę, kończę pracę...")
        break
    elif number > random_number:
        client_socket.send(smaller_message.encode())
    else:
        client_socket.send(bigger_message.encode())

client_socket.close()
