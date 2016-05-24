class MyList():
    def __init__(self, l=[]):
        self._l = l.copy()
    def __repr__(self):
        return repr(self._l)
    def __len__(self):
        return len(self._l)
    def __add__(self, value):
        self._l.append(value)
    def __setitem__(self, index, value):
        self._l[index] = value
    def __getitem__(self, index):
       if index == Ellipsis:
           return self._l.copy()
       return self._l[index]
    
