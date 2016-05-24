import numbers
class Number:
    def __iadd__(self, n):
        self.n = n
    def __repr__(self):
        return "Number ({})".format(self.n)
    def __add__(self, other):
        if not isinstance(other, numbers.Number): 
            other = other.n
        return Number(self.n + other.n)
    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self, other):
        print("Iadd")
        return self.__add__(other)
