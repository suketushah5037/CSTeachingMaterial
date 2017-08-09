import socket
import sys
import hashlib

s = socket.socket()
s.bind(("localhost", 9999))
s.listen(10)
sc, address = s.accept()

print("server")
print(address)
i = 1

f = open('serverfile_' + str(i) + ".txt", "wb")
i = i + 1

while(True):
    data = sc.recv(1024)
    print(data)

    #not keeping the server alive all the time
    f.write(data)
    f.close()
    break
print("no more data")

hashdigest = hashlib.sha256(data)
print(hashdigest)
print(hashdigest.hexdigest())
print("compare the hash received here, if same the file transfer has not corrupted the data")
sc.close()
s.close()
