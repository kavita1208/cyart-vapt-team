import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Ask user for URL
url = input("Enter target URL: ").strip()

try:
    r = requests.get(url, timeout=10)
    r.raise_for_status()

    print(f"\n[+] Web Application Found: {url}")
    print("\n[+] Discovered Links / Endpoints:\n")

    soup = BeautifulSoup(r.text, "html.parser")

    endpoints = set()

    for link in soup.find_all("a", href=True):
        endpoint = urljoin(url, link["href"])
        endpoints.add(endpoint)

    for endpoint in sorted(endpoints):
        print(endpoint)

except requests.exceptions.RequestException as e:
    print(f"[-] Error: {e}")
