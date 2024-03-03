import socket

def check_if_correct_ip_addr(ip_addr):
    try:
        packed_ip4 = socket.inet_aton(ip_addr)
        print("Correct IPv4 address")
    except socket.error:
        try:
            packed_ip6 = socket.inet_pton(socket.AF_INET6, ip_addr)
            print("Correct IPv6 address")
        except socket.error:
            print("Incorrect IP address")

ip_addr = input("Enter IP address: ")
check_if_correct_ip_addr(ip_addr)