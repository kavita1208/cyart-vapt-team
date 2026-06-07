import requests

ip = "8.8.8.8"

url = f"https://ipinfo.io/{ip}/json"

data = requests.get(url).json()

print("\nThreat Intelligence")

print("IP:", data.get("ip"))
print("City:", data.get("city"))
print("Country:", data.get("country"))
print("Org:", data.get("org"))
