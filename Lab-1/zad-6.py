import socket
import sys

def connect_to_server(address, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_address = (address, port)
        print(f"Connecting to {address} on port {port}")
        sock.connect(server_address)

        print("Successfully connected!")
    except socket.error as e:
        print(f"Connection failed: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Use inline arguments: <address> <port>!")
    else:
        address = sys.argv[1]
        port = int(sys.argv[2])
        connect_to_server(address, port)