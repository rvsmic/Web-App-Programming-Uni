import packets as p
import socket

def process_packet(packet):
    processed_packet = [p.hex_to_dec(x) for x in packet.split(' ')]

    source_port = processed_packet[0] * 256 + processed_packet[1]
    recipient_port = processed_packet[2] * 256 + processed_packet[3]
    length = processed_packet[4] * 256 + processed_packet[5]
    checksum = processed_packet[6] * 256 + processed_packet[7]
    message = "".join([p.hex_to_ascii(x) for x in processed_packet[8:]])

    print(f'Port nadawcy: {source_port}')
    print(f'Port odbiorcy: {recipient_port}')
    print(f'Długość: {length}')
    print(f'Suma kontrolna: {checksum}')
    print(f'Wiadomość: {message}')
    
    return source_port, recipient_port, length, checksum, message

sp, rp, l, ck, mess = process_packet(p.udp_datagram)

server_address = ('127.0.0.1', 2909)
message = f'zad13odp;src;{sp};dst;{rp};data;{mess}'

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