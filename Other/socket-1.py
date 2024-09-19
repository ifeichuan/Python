import socket

s = socket.socket()
host = socket.gethostbyname(locals)
print(host)