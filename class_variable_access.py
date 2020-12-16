class Test():
    a=10

    def __init__(self):
        print(self.a)
        print(Test.a)

    def m1(self):
        print(self.a)
        print(Test.a)

    @classmethod
    def m2(cls):
        print(cls.a)
        print(Test.a)

    @staticmethod
    def m3():
        print(Test.a)

t=Test()
t.m1()
Test.m2()
Test.m3()

print(t.a)
print(Test.a)
