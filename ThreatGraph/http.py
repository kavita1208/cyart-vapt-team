import requests

url = "https://circlechess.com"

response = requests.get(url, timeout=5)

print("\nURL:", url)

server = response.headers.get("Server")
powered = response.headers.get("X-Powered-By")

print("Server:", server)
print("X-Powered-By:", powered)
