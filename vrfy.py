#!/usr/bin/python
import socket
import sys

if len(sys.argv) != 3:
        print "Usage: vrfy.py <username>"
        sys.exit(0)

# Loop through SMTP Addresses

smtp_filename = sys.argv[1]

with open(smtp_filename) as ipaddressfile:
        ipcontent=ipaddressfile.readlines()
        ipaddressfile.close()

for ipline in ipcontent:
        # Create socket
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the Server
        connect=s.connect((ipline,25))
        print '=============================='
        print 'Brute Forcing Port 25 of: ' + ipline
        print '=============================='

        # Receive the banner
        banner=s.recv(1024)
        print banner

        users_filename = sys.argv[2]
        with open(users_filename) as file:
                content=file.readlines()
                file.close()
        for line in content:
                # VRFY a user
                s.send('VRFY ' + line + '\r\n')
                result=s.recv(1024)
                print result

        # Close the socket
        s.close()