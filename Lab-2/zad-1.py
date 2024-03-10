import socket
import struct
import time

NTP_SERVER = 'ntp.task.gda.pl'
NTP_PORT = 123 # 13 był błędny

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# wysłanie pustego pakietu
data = b'\x1b' + 47 * b'\0'
sock.sendto(data, (NTP_SERVER, NTP_PORT))

data, address = sock.recvfrom(1024)

ntp_time = struct.unpack('!12I', data)[10]
unix_time = ntp_time - 2208988800

formatted_time = time.ctime(unix_time)

print("Aktualna data i czas:", formatted_time)

sock.close()