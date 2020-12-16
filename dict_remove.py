#pop()
d={100:'A',200:'B',300:'C',400:'D'}

r=d.pop(100)

r2=d.pop(500,'Test')

print(r,r2,sep='\n')

print(d)

#popitem()
d.popitem()

print(d)
d.popitem()
d.popitem()
#d.popitem()

#clear()
d1={100:'A',200:'B',300:'C',400:'D'}

print(d.clear())

#setdefault()
print(d1.setdefault(500,'Sudhee'))
print(d1.setdefault(100,'Sudhee'))
print(d1)

