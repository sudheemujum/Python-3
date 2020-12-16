def fibo(n):
    if n<1:
        print('The entered number is less than 1')
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
for i in range(1,10):
    print('The fibonacci series for {} is {}'.format(i,fibo(i)))
