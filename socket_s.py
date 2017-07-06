#!/usr/bin/python3
# 文件名：server.py

# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)
i=5
while i:
    # 建立客户端连接
    clientsocket,addr = serversocket.accept()      

    print("connection addr: %s" % str(addr))
    
    msg=input('what is the order: ')
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
    i-=1
