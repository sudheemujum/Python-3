n=int(input('Enter any number:'))

if n<=1:
    print('It is not a Prime number')

else:
    is_Prime=True

    for i in range(2,n//2+1):
        if n%i==0:
            is_Prime=False
            break
    if is_Prime==True:
        print('It is a Prime number')
    else:
        print('It is not a Prime number')

    
        
