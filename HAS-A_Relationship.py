class Engine:
    def useEngine(self):
        self.power='125W'
        print('Engine specific functionality')

class Car:
    def __init__(self):
        self.engine=Engine()
    def useCar(self):
        print('Car requires Engines functionality')
        self.engine.useEngine()
        print(self.engine.power)
        

c=Car()
c.useCar()
