import select
import socket

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setblocking(False)
    server_socket.bind(('127.0.0.1', 6666))
    server_socket.listen(5)

    inputs = [server_socket]
    outputs = []
    message_queues = {}

    while inputs:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)

        for s in readable:
            if s is server_socket:
                client_socket, client_address = s.accept()
                client_socket.setblocking(False)
                inputs.append(client_socket)
                message_queues[client_socket] = []
            else:
                data = s.recv(1024)
                if data:
                    message_queues[s].append(data)
                    if s not in outputs:
                        outputs.append(s)
                else:
                    if s in outputs:
                        outputs.remove(s)
                    inputs.remove(s)
                    s.close()
                    del message_queues[s]

        for s in writable:
            try:
                message = message_queues[s].pop(0)
                s.sendall(message)
                print('Echo:', message.decode())
            except IndexError:
                outputs.remove(s)

        for s in exceptional:
            inputs.remove(s)
            if s in outputs:
                outputs.remove(s)
            s.close()
            del message_queues[s]