class Employee:

    def __init__(self, eno, ename, sal):
        self.eno=eno
        self.ename=ename
        self.sal=sal

    def display(self):
        print('The salary of {} with eno {} is {}'.format(self.ename, self.eno,self.sal))


class Manager:

    def updateEmpSal(emp):
        emp.sal=emp.sal+1500
        emp.display()

emp=Employee(100,'Sudhee',2000)
Manager.updateEmpSal(emp)
