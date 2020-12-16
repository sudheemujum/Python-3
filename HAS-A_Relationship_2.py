class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color

    def carInfo(self):
        print('The {} car has a model {} with color {}'.format(self.name,self.model,self.color))

class Employee:
    def __init__(self,name,eno,car):
        self.name=name
        self.eno=eno
        self.car=car

    def empInfo(self):
        print('Employee name:',self.name)
        print('Employee number:',self.eno)
        print('Car of the employee:')
        self.car.carInfo()

car=Car('Innova','2.5V','White')
e=Employee('Sudhee',352810,car)
e.empInfo()

        
