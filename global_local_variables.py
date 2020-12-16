#Global & local variable
a=10

def f1():
    print(a)
    b=20
    print(b)

def f2():
    print(a)
    #print(b)

f1()
f2()

#Need of global keyword

b=20

def f3():
    global b #If you don't use the global here, then value will not be changed in below functions
    b=100
    print(b)

def f4():
    print(b)

def f5():
    global b
    print(b)

f3()
f4()
f5()

#How to display global variable inside the function

a=888
def f6():
    a=999
    print(a)
    print(globals())
    print(globals()['a'],'Or you can use',globals().get('a'))

f6()




