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
        ipinfo=0
        print("Please Send your ip address",ipinfo)
        conn.send(str(ipinfo).encode())
        a = conn.recv(1024).decode("utf-8")
        print("the ip address that we recieved is"+a)
        b ="."
        A=127
        B=191
        f =([pos for pos, char in enumerate(a) if char==b])
        f1=""
        f2=""
        f3=""
        f4=""
        if(len(f)>3 or len(f)<3):
            print("Invalid Ip Address format")
        else:
            print("Valid Ip Address format")
            if(a[0]=='0' or a[f[0]+1]=='0' or a[f[1]+1]=='0' or a[f[2]+1]=='0'):
                print("It is invalid ip address (The octet cannot start with 0) ")
            else:
                print("It is a Valid String")
            for i in range(f[0]):
                f1+=a[i]
            print("First Octet is" + f1)
            F1=int(f1)
            for i in range(f[0]+1,f[1]):
                f2+=a[i]
            print("Second octet is" + f2)
            for i in range(f[1]+1,f[2]):
                f3+=a[i]
            print("Third octet is" + f3)
            for i in range(f[2]+1,len(a)):
                f4+=a[i]
            print("Forth octet is" + f4)
            if(F1<A):
                conn.send("Ip Address in Class A".encode())
                conn.send("The First Ip Address = 1.0.0.0".encode())
                conn.send("Subnet Mask = 255.0.0.0".encode())
                conn.send("The Network Mask = 255.0.0.0".encode())
            elif(F1>A and F1<B):
                conn.send("Ip Address in Class B".encode())
                conn.send("The First Ip Address = 128.0.0.0".encode())
                conn.send("Subnet Mask = 255.255.0.0".encode())
                conn.send("The Network Mask = 255.255.0.0".encode())
            elif(F1>B):
                conn.send("Ip Address in Class C".encode())
                conn.send("The First Ip Address = 192.0.0.0".encode())
                conn.send("Subnet Mask = 255.255.255.0".encode())
                conn.send("The Network Mask = 255.255.255.0".encode())
                
                
