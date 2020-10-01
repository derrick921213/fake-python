import socket
import struct
 
IP = '127.0.0.1'
PORT = 8080
ADD = (IP, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADD)
while True:
    msg = input('请输入命令（q退出）>>>>').strip()
    if not msg:continue #判断输入是否为空，确保不存在空传输等待
    client.send(msg.encode('utf-8'))
  
    # 以固定长度获取报头，即获取命令显示长度，以元组返回
    header = client.recv(4)
    msg_size = struct.unpack('i',header)[0]
    
    #循环在客户端上打印服务器命令显示
    res = b''
    recv_size = 0
    while recv_size < msg_size:
        data = client.recv(1024)
        recv_size += len(data)
        res += data
    print(res.decode('gbk'))
    # date = client.recv(1024)
    # print(date.decode('gbk'))

    if msg == 'q':
        break
client.close()