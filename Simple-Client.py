import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8118))
client.send("I am CLIENT<br>")
from_server = client.recv(4096)
client.close()
print(from_server)
