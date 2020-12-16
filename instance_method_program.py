class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print('Hello',self.name)
        print('Yor marks are',self.marks)

    def grade(self):
        if self.marks>=60:
            print('You got first grade')
        elif self.marks>=50:
            print('You got second grade')
        elif self.marks>=35:
            print('You got third grade')
        else:
            print('you are failed')

n=int(input('Enter number of students:'))

for i in range(n):
    name=input('Enter the name of the student:')
    marks=int(input('Enter the marks of the student:'))
    s=Student(name,marks)
    s.display()
    s.grade()
    print()

            
