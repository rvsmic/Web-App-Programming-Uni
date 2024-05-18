import socket

server_address = ('echo.websocket.events', 80)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(server_address)

    handshake_request = b"GET /chat HTTP/1.1\r\n"\
                        b"Host: echo.websocket.events\r\n"\
                        b"Upgrade: websocket\r\n"\
                        b"Connection: Upgrade\r\n"\
                        b"Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==\r\n"\
                        b"Origin: http://example.com\r\n"\
                        b"Sec-WebSocket-Protocol: chat\r\n"\
                        b"Sec-WebSocket-Version: 13\r\n\r\n"
    client_socket.send(handshake_request)

    response = client_socket.recv(1024)
    print(response)
    message = ''.join(format(ord(x), 'b') for x in 'Witam')
    frame = bytearray()
    frame.append(0x82)
    frame.append(int('10001100', 2))
    frame.append(0x00)
    frame.append(0x00)
    frame.append(0x00)
    frame.append(0x00)
    frame.append(0x00)
    frame.append(0x00)
    frame.append(0x00)
    frame.append(0x00)
    client_socket.settimeout(3)

    client_socket.sendall(frame)
    client_socket.sendall(message.encode())
    
    response = client_socket.recv(1024)
    print('Otrzymana odpowiedź:', response)
    
except Exception as e:
    print(e)
finally:
    client_socket.close()