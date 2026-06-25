# fingerprint.py

import requests

url = input("Enter URL (https://example.com): ").strip()

try:
    r = requests.get(url, timeout=10)

    print("\nStatus Code:", r.status_code)
    print("Server:", r.headers.get("Server", "Unknown"))
    print("Technology:", r.headers.get("X-Powered-By", "Unknown"))

except Exception as e:
    print("Error:", e)
