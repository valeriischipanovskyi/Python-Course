class A:
    def __new__(cls, a):
        self = super().__new__(cls)
        print('New ', self)
        return self
    def __init__(self, a):
        print('Init ', self)
