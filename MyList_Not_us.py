class MyList_Not_us():
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
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        if self.i == len(self._l):
            raise StopIteration
        self._l += 1
        return self._l[self.i - 1]
        
