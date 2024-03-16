import packets as p
import socket

def process_ip_packet(packet):
    processed_packet = [p.hex_to_dec(x) for x in packet.split(' ')]

    protocol_version = packet.split(' ')[0][0]
    protocol = processed_packet[9]
    source_ip = ".".join([str(x) for x in processed_packet[12:16]])
    recipient_ip = ".".join([str(x) for x in processed_packet[16:20]])
    
    remaining_packet = packet[61:]
    
    print(f'Wersja protokołu: {protocol_version}')
    print(f'Protokół: {protocol}')
    print(f'IP nadawcy: {source_ip}')
    print(f'IP odbiorcy: {recipient_ip}')

    return protocol_version, protocol, source_ip, recipient_ip, remaining_packet

def process_tcp_packet(packet):
    processed_packet = [p.hex_to_dec(x) for x in packet.split(' ')]

    source_port = processed_packet[0] * 256 + processed_packet[1]
    recipient_port = processed_packet[2] * 256 + processed_packet[3]
    length = processed_packet[4] * 256 + processed_packet[5]
    checksum = processed_packet[6] * 256 + processed_packet[7]
    message = "".join([p.hex_to_ascii(x) for x in processed_packet[32:]])

    print(f'Port nadawcy: {source_port}')
    print(f'Port odbiorcy: {recipient_port}')
    print(f'Długość: {length}')
    print(f'Suma kontrolna: {checksum}')
    print(f'Wiadomość: {message}')
    
    return source_port, recipient_port, message

protv, prot, sip, rip, remaining_packet = process_ip_packet(p.ip_packet)

server_address = ('127.0.0.1', 2911)
message1 = f'zad15odpA;ver;{protv};srcip;{sip};dstip;{rip};type;{prot}'

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
    sp, rp, mess = process_tcp_packet(remaining_packet)
    message2 = f'zad15odpB;srcport;{sp};dstport;{rp};data;{mess}'
    try:
        sock.sendto(message2.encode(), server_address)
        data, server = sock.recvfrom(1024)
        response = data.decode()
        print('Odpowiedź serwera:', response)
    except ConnectionRefusedError:
        print('Błąd połączenia')
    finally:
        sock.close()