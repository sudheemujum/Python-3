class Student:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def setMarks(self,marks):
        self.marks=marks

    def getMarks(self):
        return self.marks

n=int(input('Enter the number of students:'))

students=[]

for i in range(n):
    s=Student()
    name=input('Enter the name of the student:')
    marks=int(input('Enter the marks for the student:'))
    s.setName(name)
    s.setMarks(marks)
    students.append(s)

for j in students:
    print('Hi:',j.getName())
    print('Your marks are:',j.getMarks())
    print()

    
      
    
