import socket

host = input("Host: ")

for port in [22, 80, 443]:
    s = socket.socket()
    s.settimeout(1)

    result = s.connect_ex((host, port))

    if result == 0:
        print(f"Port {port}: Open")
    else:
        print(f"Port {port}: Closed")

    s.close()
