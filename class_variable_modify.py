class Test():
    a=10

    def __init__(self):
        Test.a=20

    def m1(self):
        Test.a=30

    @classmethod
    def m2(cls):
        Test.a=40
        cls.a=50

    @staticmethod
    def m3():
        Test.a=60

t=Test()
t.m1()
Test.m2()
Test.m3()
print(t.a)
