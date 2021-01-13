import socket

HOST = '127.0.0.1'
PORT = 4646

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    conn.connect((HOST, PORT))
    print("connection established")
    msg = conn.recv(1024).decode("utf-8")
    print(msg)
    print("Mind that the Program is only for Classes A,B & C")
    wc = input("Please input an ip address ")
    conn.send(wc.encode())
    print(conn.recv(1024).decode("utf-8"))
    print(conn.recv(1024).decode("utf-8"))
    print(conn.recv(1024).decode("utf-8"))
    print(conn.recv(1024).decode("utf-8"))