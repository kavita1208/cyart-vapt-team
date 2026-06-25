import socket
import whois
from urllib.parse import urlparse

url = input("Enter URL: ").strip()

domain = urlparse(url).netloc or url

try:
    ip = socket.gethostbyname(domain)

    w = whois.whois(domain)

    asset = {
        "Domain": domain,
        "Owner": w.registrar,
        "IP Address": ip,
        "Technology": "Unknown",
        "Risk": "Low"
    }

    print("\nAsset Information")
    print("-" * 30)

    for k, v in asset.items():
        print(f"{k}: {v}")

except Exception as e:
    print("Error:", e)
