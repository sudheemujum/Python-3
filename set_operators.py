t1={10,20,30,40}
t2={30,40,50,60}

#Union
t3=t1.union(t2)

print(t3)

t4=t1|t2

print(t4)

#Intersection

t5=t1.intersection(t2)
print(t5)

t6=t1 & t2

print(t6)

#difference

t7=t1.difference(t2)
print(t7)

t8=t1-t2

print(t8)

#Symmetric difference
t1={10,20,30,40}
t2={10,50,30,60}
t3=t1.symmetric_difference(t2)
t4=t1^t2

print(t3)
print(t4)



