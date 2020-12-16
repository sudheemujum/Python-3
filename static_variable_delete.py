class Test():
    a=10
    
    def __init__(self):
        Test.b=20
        del Test.a

    def m1(self):
        Test.c=30
        del Test.b

    @classmethod
    def m2(cls):
        Test.d=40 #or cls.d=40
        del Test.c #or cls.c

    @staticmethod
    def m3():
        Test.e=50
        del Test.d

t=Test()
t.m1()
t.m2()
t.m3()
print(Test.__dict__)
