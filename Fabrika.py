class Car:
    def run(self):
        print('RRRRR')
        
class Truck:
    def run(self):
        print('BZZZZ')
        
vehicles = ['Car', 'Car', 'Truck', 'Car']

class Vehicle:
    def __new__(cls, type_):
        if type_ == 'Car':
            return Car()
        elif type_ == 'Truck':
            return Truck()
        else:
            raise ValueError
