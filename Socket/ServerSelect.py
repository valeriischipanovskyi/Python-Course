import socket
import select
import random

def handle(c, r):
    while True:
        data = c.recv(1024)
        if not data:
            connections.remove(c)
            c.close()
            return
        print(data, r)
        c.sendall(data)

s = socket.socket()
s.bind(('localhost', 8000))
s.listen(5)
s.setblocking(False)
print('Starting')
connections = [s]
while True:
    r_s, _, _ = select.select(connections, [], [])
    for socket in r_s:
        if socket == s:
            c, a = s.accept()
            print('Connect{}'.format(a))
            connections.append(c)
        else:
            handle(socket, random.random())
