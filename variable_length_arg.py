#Variable lenth arguments

def f1(*n):
    print(type(n))
    print(n)

f1()

f1((10,20),(30,40))

#Find some of all the entered numbers

def f2_sum(*n):
    sum=0
    for i in n:
        sum=sum+i
    print('The sum is:',sum)

f2_sum(10)
f2_sum(10,30,50)


def f3(x,*y):
    print(x)
    print(y)

f3(10,20,30,40)

def f4(*x,y):
    print(x)
    print(y)

#f3(10,20,30,40) -> Error
f4(10,20,30,y=40)

#def f5(*x,*y) -> Invalid
        
