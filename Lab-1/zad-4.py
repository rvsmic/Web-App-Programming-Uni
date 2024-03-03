import socket

def get_hostname(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)
        return hostname[0]
    except socket.herror:
        return "Can't find hostname for this IP address"

ip_address = input("Enter IP address: ")
print(get_hostname(ip_address))