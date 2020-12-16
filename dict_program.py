#Program to enter name and marks of the student

n=int(input('Enter the number of students:'))

d={}

for x in range(n):
    name=input('Enter the name of the student:')
    marks=int(input('Enter the marks of the student:'))
    d[name]=marks
print('*'*30)
print('Name','\t\t','marks')
print('*'*30)

for name in d:
    print(name,'\t\t',d[name])
