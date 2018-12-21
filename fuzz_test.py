#!/usr/bin/python

import socket

buffers = ["A"]

counter = 20

while len(buffers) <= 30: # how many elements in the array
        buffers.append("A"*counter) #creates new buffer in the array
        counter=counter+100  #add 100 to the next buffer
for string in buffers:
        print "Buffer string length: " + str(len(string)) # each buffer element "string" in the buffers array

