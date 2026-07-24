import socket

host = input("website likho: ")

s = socket.socket()

result = s.connect_ex((host, 443))

if result == 0:
    print("Port 443 Open")
else:
    print("Port 443 Closed")

s.close()
