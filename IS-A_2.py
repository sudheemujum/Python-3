class P:
    a=10
    def __init__(self):
        print('parent constructor')
        self.b=20

    def m1(self):
        print('parent instance method')
    @classmethod
    def m2(cls):
        print('parent class method')
    def m3():
        print('parent static method')

class C(P):
    pass

c=C()
print(c.a)
print(c.b)
c.m1()
c.m2()

        
