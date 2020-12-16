l=[10,10,20,10,30,20,40,10]
s=set(l)
l1=list(s)

print(l)
print(s)
print(l1)

l2=[]

for x in l:
    if x not in l2:
        l2.append(x)
print(l2)
