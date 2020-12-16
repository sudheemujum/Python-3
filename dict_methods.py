d={100:'A',200:'B',300:'C'}

print(len(d))

#Get method
print(d.get(300))
print(d.get(700))
print(d.get(500,'Guest'))

#update
d1={100:'A',200:'B'}
d2={300:'C',100:'Sudhee'}
d1.update(d2)

print(d1)

#keys()
k=d.keys()
print(k)

for key in k:
    print(key)

#values()
v=d.values()
print(v)

for value in v:
    print(value)

#items()

i=d.items()
print(i)

for item in i:
    print(item)

for k,v in i:
    print(k,'.......',v)


