class Test:

    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
        
    def m1(self):
        self.e=30
        del self.c #Deleting inside a method

t1=Test() #a, b, c and d will be added to the object
t1.m1() #e will be added to the object & c will be deleted

t1.a=888
t1.b=999 #Updating the instance variable
t1.f=40 #d will be added to the object

print(t1.a,t1.b,t1.d,t1.e,t1.f) #Accessing the instance variables 

t2=Test()
del t2.a #a will be deleted in t2

print(t2.b,t2.c,t2.d)

print(t1.__dict__)
print(t2.__dict__)
