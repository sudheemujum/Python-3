cart=[10,20,40,50,100,200,50]
for item in cart:
    if item>100:
        print('Insurance is required in break')
        break
    print(item)

for item2 in cart:
    if item2>100:
        print('Insurance is required in continue')
        continue
    print(item2)
    
#Nested loops

for i in range(3):
    for j in range(3):
        if i==j:
            break
        print(i,j)
        

for i in range(3):
    for j in range(3):
        if i==j:
            continue
        print(i,j)
