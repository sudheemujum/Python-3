

if __name__=='__main__':
    print('Direct execution like main program')
else:
    print('Indirect execution because of import statement')


def f1():
    print('f1 function')

def f2():
    print('f2 function')

def f3():
    print('f3 function')

if __name__=='__main__':
    f1()
    f2()
    f3()
