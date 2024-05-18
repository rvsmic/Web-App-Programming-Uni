import requests

name = input("Podaj imię: ")
email = input("Podaj email: ")

data = {
    "name": name,
    "email": email
}

response = requests.post("http://httpbin.org/post", data=data)

print(response.text)