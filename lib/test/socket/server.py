import socket
host = '127.0.0.1'
port = 8001

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
class goto(Exception): pass
try:
    while True:
        conn,addr = s.accept()
        print('Connected by',addr)
        while True:
            data = conn.recv(1024)
            print(data.decode())
            if data == "Close":
                raise goto
            conn.send("Server received you message".encode('utf-8'))
except goto:
    s.close()        
