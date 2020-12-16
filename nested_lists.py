#Nested lists:
l1=[10,20,30,40]
l2=[50,60,70]

l1.append(l2)

print(l1)

print(l1[4][0])

l3=[[10,20,30,['A','B','C']],[40,50,60],[70,80,90]]

print('Elements row wise')

for x in l3:
    print(x)
print('Print elements in matrix style')

for x in l3:
    for y in x:
        print(y, end=' ')
    print('')

    
    
