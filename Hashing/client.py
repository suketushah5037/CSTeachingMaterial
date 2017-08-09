import hashlib
import socket
import sys

print(hashlib.algorithms_available)

print("client")
s= socket.socket()
s.connect(("localhost",9999))
f = open("clientfile.txt", "rb")
data=f.read(1024)
while(1):
    if not data:
        f.close()
        s.close()
        break
    hashdigest = hashlib.sha256(data)
    print(hashdigest)
    print(hashdigest.hexdigest())

    s.send(data)
    data = f.read(1024)
        
