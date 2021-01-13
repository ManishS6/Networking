import socket
import datetime
HOST = '127.0.0.1'
PORT = 4646

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        ws = conn.recv(1024).decode("utf-8")
        frame = 0
        while(frame < int(ws)):
            for i in range(int(ws)):
                print("Frame Transmitted:",frame)
                conn.send(str(frame).encode())
                frame += 1
                if frame == int(ws):
                    break
            ack = int(input("Please Input NACK:"))
            if ack == int(ws):
                break
            else:
                frame = ack
