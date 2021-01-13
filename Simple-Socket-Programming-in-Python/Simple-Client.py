import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8118))
a = "I am a Client"
client.send(str(a).encode())
from_server = client.recv(4096).decode()
client.close()
print(from_server)
