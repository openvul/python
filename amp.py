#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import threading
import time
import struct
import os

def gettime():
    now = time.strftime('%m-%d %H:%M:%S',time.localtime(time.time()))  
    return now

def function(newsock, address):  
    FILEINFO_SIZE = struct.calcsize('128sI')
    try:  
        fhead = newsock.recv(FILEINFO_SIZE)  
        filename, filesize = struct.unpack('128sI', fhead)
        filename = filename.strip('\00')
        path = "repos"
        isExists=os.path.exists(path)
        if not isExists:
            os.makedirs(path)
        restsize = filesize
        if len(filename) > 0 and filesize > 0:
            fp = open(path + "/" + filename,'wb')
            print "["+ gettime() +"] 文件接收开始-> " + filename + " [Size：" + str(filesize/1024) + " kb]"
            while True:  
                if restsize > 1024:#如果剩余数据包大于1024，就去1024的数据包  
                    filedata = newsock.recv(1024)  
                else:  
                    filedata = newsock.recv(restsize)  
                    fp.write(filedata)  
                    break  
                if not filedata:  
                    break  
                fp.write(filedata)  
                restsize = restsize - len(filedata)#计算剩余数据包大小  
                if restsize <= 0:
                    break
            fp.close()
            print "["+ gettime() +"] 文件接收完成-> " + filename + " [Size：" + str(filesize/1024) + " kb]"
    except Exception as e:
        print "%s" % str(e)
    finally:
        newsock.close()

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#创建tcp连接
port = 1337
sock.bind(('0.0.0.0',port))#绑定端口和ip
sock.listen(5)#监听
print "["+ gettime() +"] 监听端口: " + str(port) + " 已完成"
while True:  
    newsock, address = sock.accept()
    print "["+ gettime() +"] 新的客户端已连入: " + str(address)
    sThread = threading.Thread(target=function,args=(newsock,address)) #如果接收到文件，创建线程  
    sThread.start()#执行线程
print 'end'