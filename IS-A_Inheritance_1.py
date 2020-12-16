class P:
    def m1(self):
        print('Parent class')

class C(P):
    def m2(self):
        print('Child class')

c=C()
c.m1()
c.m2()
