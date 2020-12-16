#Variable length key word arguments

def f1(**kwargs):
    print(kwargs)

f1()
f1(a=10,b=20)

def f2(*args, **kwargs):
    print(args)
    print(kwargs)

f2(10,20,name='Sudhee',city='Agadi')
            
