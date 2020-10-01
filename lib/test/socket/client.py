import socket 
host = '127.0.0.1'
port = 8001
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while True:
    msg = input("Please input msg:")
    if msg == '':
        s.send("Close".encode('utf-8'))
        break
    s.send(msg.encode('utf-8'))
    data = s.recv(1024)
    print(data.decode())
s.close()    