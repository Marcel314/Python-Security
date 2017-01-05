__author__ = 'Marcelo'

import socket

target_host = "www.google.com"
target_port = 80

# Create a IP4 TCP socket object.
client = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

# Connect to the client.
client.connect((target_host,target_port))

# Send data.
# In Python 3, the socket accepts bytes, you need to convert string to bytes with a str.encode() function.
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode())

# receive data
response = client.recv(4096)

print("response = ",response)
