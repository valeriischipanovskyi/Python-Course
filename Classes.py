import functools
@functools.total_ordering
class Persson:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return "{} {}".format(self.name, self.age)
    def __str__(self):
        return "<{} {}>".format(self.name, self.age)
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    def __lt__(self, other):
        return self.name < other.name
