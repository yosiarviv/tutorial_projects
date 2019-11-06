import socket

HOST = socket.gethostbyname(socket.gethostname())
print(HOST)

print(socket.getfqdn())