#Remove

l1=[1,2,3,4,5,6]

l1.remove(1)

print(l1)

l2=[1,1,1,2,1,2,3,4,1]

x=int(input('Enter the number to remove:'))

while True:
    if x in l2:
        l2.remove(x)
    else:
        break

print('l1 after removal:',l2)

l2=[10,20,30]

print(l2.pop())
print(l2.pop())
print(l2.pop())
#print(l2.pop()) -> Index error

l3=[10,30,20,50]

l3.pop(2)

print(l3)
