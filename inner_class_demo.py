class Outer:

    def __init__(self):
        print('Outer object creation')

    class Inner:

        def __init__(self):
            print('Inner class object creation')

        def m1(self):
            print('Inner class method')


o=Outer()
i=o.Inner() #another way is i=Outer().Inner()
i.m1() #another method is Outer().Inner().m1()

#Outer().Inner().m1()
