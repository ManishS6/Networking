import socket

HOST = '127.0.0.1'
PORT = 4646

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    conn.connect((HOST, PORT))
    print("connection established")
    wc = input("Please Input Size of window ")
    conn.send(wc.encode())
    c = 0
    while(True):
        conn.recv(1024).decode("utf-8")
        c+=1
        if c == int(wc):
            print("All frames are successfully recieved")
