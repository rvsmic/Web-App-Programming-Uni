import socket

def check_syntax(txt):
    s = len(txt.split(";"))
    if s != 7:
        return "BAD_SYNTAX"
    else:
        tmp = txt.split(";")
        if tmp[0] == "zad14odp" and tmp[1] == "src" and tmp[3] == "dst" and tmp[5] == "data":
            try :
                src_port = int(tmp[2])
                dst_port = int(tmp[4])
                data = tmp[6]
            except :
                return "BAD_SYNTAX"
            if src_port == 2900 and dst_port == 35211 and data == "hello :)":
                return "TAK"
            else:
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
        data = data.decode()
        print(f"Odebrana wiadomość od {address}: {data}")
        answer = check_syntax(data)
        print("Wysyłam odpowiedź:", answer)
        sent = server_socket.sendto(answer.encode(), address)