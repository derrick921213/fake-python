import socket
import subprocess
import struct
 
IP = '127.0.0.1'
PORT = 8080
ADD = (IP, PORT)
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADD)
server.listen(5)
while True:
    conn, addr = server.accept()
    while True:
        try:  # 针对win系统
            #接受客户端指令
            date = conn.recv(1024)
            if not date: break  # 针对linux系统
            date = date.decode('utf-8')
            if date == 'q':
                conn.send('已退出'.encode('gbk'))
                break
           
            #系统执行命令，并保存显示用于返回客户端
            obj = subprocess.Popen(date, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(obj)
            #命令显示
            out = obj.stdout.read()
            #错误显示
            err = obj.stderr.read()
            
            msg = err + out
            msg_size = len(out) + len(err)
            #固定长度（4）打包作为报头传输
            size = struct.pack('i', msg_size)
            conn.send(size + msg)
            # conn.send(msg)  # 以gbk 的bytes进行发送
            # conn.send(err)
        except ConnectionResetError:
            break
    conn.close()