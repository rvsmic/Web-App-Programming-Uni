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

    response = client_socket.recv(4096)
    print('Odpowiedź handshake:', response)
except Exception as e:
    print(e)
finally:
    client_socket.close()