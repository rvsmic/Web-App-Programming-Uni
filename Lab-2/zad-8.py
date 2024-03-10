import socket
import sys

def scan_ports(host):
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            service = socket.getservbyport(port)
            print(f"Port {port} is open! Service: {service}")
        else:
            print(f"Port {port} is closed!")
        sock.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use inline arguments: <address>!")
    else:
        host = sys.argv[1]
        scan_ports(host)
