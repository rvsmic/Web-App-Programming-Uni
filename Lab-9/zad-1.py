import requests

url = 'http://httpbin.org/html'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    with open('output.html', 'w') as file:
        file.write(response.text)
        print('HTML file saved successfully.')
else:
    print('Failed to retrieve HTML content.')