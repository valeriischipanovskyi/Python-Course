import multiprocessing

a = 0
def f():
    global a
    for i in range(10000):
       a += 1
    print(a)

for i in range(10):
    p = multiprocessing.Process(target=f, args=(i,))
    p.start()
print(a)
