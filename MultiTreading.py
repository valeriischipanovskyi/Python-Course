import threading
import urllib.request

def f():
    r = urllib.request.urlopen('http://mail.ru')
    print (len(r.read()))

ts = []
for i in range(20):
    t = threading.Thread()
    t.start()
    for t in ts:
        t.join()
