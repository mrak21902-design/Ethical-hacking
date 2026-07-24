import socket 

website = input("Website ka namam likho: ")

ip = socket.gethostbyname(website)

print("IP Address:", ip)
