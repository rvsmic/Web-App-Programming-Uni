#!/usr/bin/env python

import socket, select, sys
from time import gmtime, strftime


def check_A_syntax(txt):
    s = len(txt.split(";"))
    if s != 9:
        return "BAD_SYNTAX"
    else:
        tmp = txt.split(";")
        if tmp[0] == "zad15odpA" and tmp[1] == "ver" and tmp[3] == "srcip" and tmp[5] == "dstip" and tmp[7] == "type":
            try:
                ver = int(tmp[2])
                srcip = tmp[4]
                dstip = tmp[6]
                type = int(tmp[8])
                if ver == 4 and type == 6 and srcip == "212.182.24.27" and dstip == "192.168.0.2":
                    return "TAK"
                else:
                    return "NIE"
            except:
                return "NIE"
        else:
            return "BAD_SYNTAX"


def check_B_syntax(txt):
    s = len(txt.split(";"))
    if s != 7:
        return "BAD_SYNTAX"
    else:
        tmp = txt.split(";")
        if tmp[0] == "zad15odpB" and tmp[1] == "srcport" and tmp[3] == "dstport" and tmp[5] == "data":

            try:
                srcport = int(tmp[2])
                dstport = int(tmp[4])
                data = tmp[6]

                if srcport == 2900 and dstport == 47526 and data == "network programming is fun":
                    return "TAK"
                else:
                    return "NIE"
            except:
                return "NIE"
        else:
            return "BAD_SYNTAX"


HOST = '127.0.0.1'
PORT = 20202

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
print(f"Serwer nasłuchuje na {HOST}:{PORT}")

while True:
    data, address = server_socket.recvfrom(1024)

    if data:
        tmp = data.decode().split(";")
        print(f"Odebrana wiadomość od {address}: {data}")

        if tmp[0] == "zad15odpA":
            answer = check_A_syntax(data.decode())
            print("Wysyłam odpowiedź: ", answer)
            sent = server_socket.sendto(answer.encode(), address)
        elif tmp[0] == "zad15odpB":
            answer = check_B_syntax(data.decode())
            print("Wysyłam odpowiedź: ", answer)
            sent = server_socket.sendto(answer.encode(), address)
        else:
            print("Wysyłam odpowiedź: BAD_SYNTAX")
            sent = server_socket.sendto("BAD_SYNTAX".encode(), address)

