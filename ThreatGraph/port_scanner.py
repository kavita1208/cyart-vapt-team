import socket

TARGET = "circlechess.com"

ports = [21, 22, 80, 443]

print(f"\nScanning {TARGET}\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((TARGET, port))

    if result == 0:
        print(f"[OPEN] Port {port}")
    else:
        print(f"[CLOSED] Port {port}")

    sock.close()
