class Lenght:
    def __set__(self, obj, value):
        obj._l = value * 100
    def __get__(self, obj, objtype):
        return obj._l / 100
    
class Line:
    length = Lenght()
    def __init__(self):
        self._l = 0
