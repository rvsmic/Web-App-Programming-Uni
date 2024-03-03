import socket

def get_ip_addr(hostname):
    try:
        ip_addr = socket.gethostbyname(hostname)
        return ip_addr
    except socket.gaierror:
        return "Can't find IP address for this hostname"

hostname = input("Enter hostname: ")
print(get_ip_addr(hostname))