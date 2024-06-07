import select
import socket
import json

API_KEY = 'd4af3e33095b8c43f1a6815954face64'
WEATHER_URL = f'http://api.openweathermap.org/data/2.5/weather?q=Lublin,pl&appid={API_KEY}'

def get_weather(command):
    weather_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    weather_socket.connect(('api.openweathermap.org', 80))
    request = f"GET /data/2.5/weather?q=Lublin,pl&appid={API_KEY} HTTP/1.1\r\nHost: api.openweathermap.org\r\n\r\n"
    weather_socket.sendall(request.encode())
    response = weather_socket.recv(4096).decode()
    weather_socket.close()

    if response.startswith('HTTP/1.1 200 OK'):
        weather_data = json.loads(response.split('\r\n\r\n')[1])
        wind_info = f"Prędkość wiatru: {weather_data['wind']['speed']} m/s, Kierunek: {weather_data['wind']['deg']} stopni, Zmienna: {weather_data['wind']['gust']} m/s"
        weather_info = f'Opis: {weather_data["weather"][0]["description"]}'
        temp_info = f'Temperatura: {weather_data["main"]["temp"] - 273.15}, Odczuwalna: {weather_data["main"]["feels_like"] - 273.15}, Min: {weather_data["main"]["temp_min"] - 273.15}, Max: {weather_data["main"]["temp_max"] - 273.15}'
        hum_info = f'Wilgotność: {weather_data["main"]["humidity"]}%'
        pres_info = f'Ciśnienie: {weather_data["main"]["pressure"]} hPa'
        if command == 'WIND':
            return wind_info
        elif command == 'WEATHER':
            return weather_info
        elif command == 'TEMP':
            return temp_info
        elif command == 'HUM':
            return hum_info
        elif command == 'PRES':
            return pres_info
        elif command == 'FULL':
            return ';\n'.join([weather_info, temp_info, wind_info, hum_info])
        elif command == 'EXIT':
            return 'Zakończono połączenie'
        else:
            return "Nieznana komenda"
    else:
        return "Nie udało się odczytać danych pogodowych"

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
                    command = data.decode().strip()
                    weather_info = get_weather(command)
                    message_queues[s].append(weather_info.encode())
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
                print('Odesłano:', message.decode())
            except IndexError:
                outputs.remove(s)

        for s in exceptional:
            inputs.remove(s)
            if s in outputs:
                outputs.remove(s)
            s.close()
            del message_queues[s]