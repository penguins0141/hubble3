#!/bin/bash

for name in {200..250};do
     ping -c 1 192.168.17.$name | grep "bytes from" | cut -d" " -f4 | cut -d":" -f1  &
done

=======Python-===============

#!/usr/bin/env python2.5
import subprocess

pingcmd = "ping -c 1 "
networkportion = "192.168.17."
startip = 200
endip = 254

print "Beginning Ping..."

for i in range(startip,endip):
     ipaddress = networkportion + str(i)
     ret = subprocess.call(pingcmd + ipaddress, shell=True, stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT)
    
     if ret == 0:
          print ipaddress + " is alive"
     else:
          print ipaddress + " did not respond"
 



