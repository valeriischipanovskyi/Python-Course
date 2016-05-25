# class Lenght:
#     def __set__(self, obj, value):
#         obj._l = value * 100
#     def __get__(self, obj, objtype):
#         return obj._l / 100
# 
# class Line:
#     length = Lenght()
#     def __init__(self):
#         self._l = 0
        
class Line:
    def __init__(self):
        self._l = 0
    @property
    def length(self):
        return self._l / 100
    @length.setter
    def length(self, value):
        self._l = value * 100
