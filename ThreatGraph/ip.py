import socket

target = input("Enter Domain: ")

try:
    ip = socket.gethostbyname(target)

    print("\n[+] Domain :", target)
    print("[+] IP Address :", ip)

except Exception as e:
    print("[-] Error:", e)
