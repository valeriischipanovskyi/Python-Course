import socket
import threading
import random

def handle(c, r):
    while True:
        data = c.recv(1024)
        if not data:
            c.close()
            break
        print(data, r)
        c.sendall(data)

s = socket.socket()
s.bind(('localhost', 8000))
s.listen(5)
print('Starting')
while True:
    c, a = s.accept()
    print('Connect{}'.format(a))
    t = threading.Thread(target=handle, args=(c, random.random()))
    t.start()
