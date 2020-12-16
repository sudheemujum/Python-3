#Dictionary basics

l1=[(100,'A'),(200,'B'),(300,'C')] #List of tuples
l2=((100,'A'),(200,'B'),(300,'C')) #Tuple of tuples
l3={(100,'A'),(200,'B'),(300,'C')} #Set of tuples
l4=[[100,'A'],[200,'B'],[300,'C']] #List of lists
l5=([100,'A'],[200,'B'],[300,'C']) #Tuple of lists
#l={[100,'A'],[200,'B'],[300,'C']} #Set of lists is un hashable

d1=dict(l1)

print(d1)

d2=dict(l2)

print(d2)

d3=dict(l3)

print(d3)

d4=dict(l4)

print(d4)

d5=dict(l5)

print(d5)

#Dynamic input
d6=eval(input('Enter dictionary:'))
print(d6)
