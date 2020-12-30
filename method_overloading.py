class Test:

    def m1(self,a=None,b=None,c=None):
        if a is not None and b is not None and c is not None:
            print('Three argument method')
        elif a is not None and b is not None:
            print('Two argument method')
        elif a is not None:
            print('One argument method')
        else:
            print('No-argument method')

t=Test()
t.m1()
t.m1(10)
t.m1(10,20)
t.m1(10,20,30)

class Test2:
    def m2(self, *args):
        print('Variable length argument methods')

t1=Test2()
t1.m2()
t1.m2(10)
t1.m2(10,20,30,40)

class Test3:
    def __init__(self,*args):
        print('Variable argument constructor method')

t3=Test3(10,20)
                  
