#1) implement a TCP server that listen on port 8900 and returns "hello"Use socket module

import socket
serversocket = socket.socket()
print("Socket connected")
port = 8900

serversocket.bind(('', port))
print("Socket bound to %s" %(port))

serversocket.listen(5)
print("Socket is listening")
print("Hello")

while True:
 c, addr = serversocket.accept()
 print("Got connection from %s" %(addr))
 c.send("Hi...")
 c.close()
