#Without recursion

def fact(n):
    result=1
    while n>=1:
        result=result*n
        n-=1
    return result

print(fact(3))
op=fact(5)
print('Factorial value is:',op)

#With recursion

def fact2(n):
    print('Executing Factorial Function with n value:',n)
    if n==0:
        result=1
    else:
        result=n*fact2(n-1)
    print('Returning result of factorial({}) is:{}'.format(n,result))
    return result

fact2(3)

#for i in range(1,4):
#    print('Factorial value of {} is {}'.format(i,fact2(i)))
        
