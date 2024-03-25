import socket
import sys

def check_service(address, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        server_address = (address, port)
        print(f"Connecting to {address} on port {port}")
        sock.connect(server_address)
        
        service_name = socket.getservbyport(port)
        print(f"Connected to service {service_name} on port {port}")
        
        message = "This is a test message"
        sock.sendall(message.encode())
        
        received_message = sock.recv(len(message)).decode()
        print(f"Received message: {received_message}")
        
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
        check_service(address, port)