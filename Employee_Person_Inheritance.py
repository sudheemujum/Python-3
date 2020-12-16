class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def personWork(self):
        print('Performs everyday routine')

class Employee(Person):
    def __init__(self,name,age,eno):
        self.name=name
        self.age=age
        self.eno=eno

    def empInfo(self):
        print('Employee name is:',self.name)
        print('Employee age and emp number is:',self.age,self.eno)

emp=Employee('Sudhee',41,34161)
emp.empInfo()
emp.personWork()
