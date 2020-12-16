t={1,2,3,4,5,6}

n=eval(input('Enter the number to be removed:'))

if n in t:
    t.remove(n)
    print(t)

else:
    print('Enetered number is not available')

t={1,2,3,4,67,34,21,13,89,123}

t.pop()

print(t)

t.clear()

print(t)
