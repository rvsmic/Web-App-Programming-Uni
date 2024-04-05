import socket
from time import sleep
from itertools import permutations

ping_message = 'PING'.encode()

def send_ping(sock, port):
    try:
        sock.connect(('127.0.0.1', port))
        sock.send(ping_message)
        sleep(1)
        data = sock.recv(1024).decode()
        if data == 'PONG':
            print(f'Uzyskano odpowiedź: {port}')
            return True
        return False
    except Exception as e:
        print("Error:", e)
        return False

def get_message():
    msgsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        msgsock.connect(('127.0.0.1', 2913))
        msgsock.settimeout(5)
        msgsock.send(ping_message)
        data = msgsock.recv(1024).decode()
        msgsock.close()
        return data
    except Exception as e:
        msgsock.close()
        return None


def port_knocking():
    ports_list = (i * 1000 + 666 for i in range(0, 65))
    open_ports = []

    print("Przeszukiwanie...")
    for port in ports_list:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # czasami nie działało na mniejszym timeoucie
        sock.settimeout(10)
        try:
            sock.connect(('127.0.0.1', port))
            sock.send(ping_message)
            data = sock.recv(1024).decode()
            if data == 'PONG':
                print(f'Znaleziono port: {port}')
                open_ports.append(port)
        except Exception as e:
            continue
        sock.close()
    print(f'Znalezione porty: ', open_ports)

    sequences = permutations(open_ports, len(open_ports))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # często pomijało dobrą konfigurację na mniejszym timeoucie
    sock.settimeout(10)

    print("Pukanie...")
    for sequence in sequences:
        sleep(2)
        print(f'Próbuję sekwencję: {sequence}')
        success_count = 0
        for port in sequence:
            success = send_ping(sock, port)
            sleep(2)
            if not success:
                break
            else:
                success_count += 1
        if success_count == len(sequence):
            data = get_message()
            if data:
                print(f"Odkryto konfigurację! -> {sequence}")
                print(f"Otrzymana wiadomość: {data}")
                break
            else:
                print("Błędna konfiguracja")
    sock.close()
    print("Koniec pukania")


port_knocking()
