__author__ = 'marcel.dominguez'

import socket

target_host = "www.google.com"
target_port = 80

# Create a socket object.
client = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

# Send data.
# In Python 3, the socket accepts bytes, you need to convert string to bytes with a str.encode() function.
client.sendto("AABBCCDD".encode(),(target_host,target_port))

# Receive data.
data, addr = client.recvfrom(4096)
