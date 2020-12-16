def fact(n):
    res=1
    while n>=1:
        res=res*n
        n-=1
    return(res)
    

for i in range(1,9):
    print('The factorial of:', i, 'is',fact(i))
