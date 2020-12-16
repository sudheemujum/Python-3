l=[0,1,2,3,4,5,6,7,8,9]

even=list(filter(lambda n:n%2==0,l))
print(even)

odd=list(filter(lambda n:n%2!=0,l))
print(odd)

nby3odd=list(filter(lambda n:n%3==0 and n%2!=0, l))

print(nby3odd)
