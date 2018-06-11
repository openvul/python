#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import os
import sys
import struct

HOST = '172.16.24.92'
PORT = 1337
BUFFER_SIZE = 1024

def send_file(file_path):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    server_address = (HOST, PORT)
    sock.connect(server_address)
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    print file_name,file_size
    try:
        print "[+]成功连接服务端",server_address   
        fhead = struct.pack('128sI',file_name,file_size)#按照规则进行打包    
        sock.send(fhead)#发送文件基本信息数据   
        print "[+]文件传输开始" 
        fp = open(file_path,'rb')    
        while True:     #发送文件    
            filedata = fp.read(BUFFER_SIZE)    
            if not filedata:    
                break    
            sock.send(filedata)
        
        print "[+]文件传输结束"
    except Exception as e:
        print "%s" % str(e)
    finally:
        fp.close()
        sock.close()

if __name__ == '__main__':
     if(len(sys.argv) < 2):
      print("Usage: python send.py send.zip")
      exit(1)
     send_file(sys.argv[1])