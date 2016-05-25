class A:
    def m1(self):
        print('A.m1')
    def m2(self):
        print('A.m2')
class Proxy:
    def __init__(self):
        self._a = A()
        def m1(self):
            print('Proxy.m1')
        def m3(self):
            print('Proxy.m3')
        def __getattr__(self, name):
            return getattr(self._a, name)
