class Scale:
    def __init__(self, n):
        self.n = n
    def __call__(self, f):
        def wrapper(x):
            return f(self.n * x)
        return wrapper
