class Shape:
    def __init__(self, pos):
        self.pos = pos

class Circle(Shape):
    def __init__(self, pos, r):
        super().__init__(pos)
        self.r = r

    def __repr__(self):
        return "Circle({}, {})".format(self.pos, self.r)
