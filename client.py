#! /usr/bin/python
import socket
host="127.0.0.1"
port=12345
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
print("ENTER NO TO BE SENT:")
a=raw_input()
s.sendall(a)
data=s.recv(1024)
s.close()
print("RECIEVED DATA :",data)
