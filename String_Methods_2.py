#Replacement operation
s='learning Pythin is  Very easy'
s1=s.replace(' ','')

print('Count of spaces is:',s.count(' '))
print('Count of spaces is:',len(s)-len(s1))


print('Before replacement:',id(s))
print('After replacement:',id(s1))

#Splitting of Strings

s='Sudee;Mujumdar;Agadi;Haveri'
l=s.split(';')

print(l)
for x in l:
    print(x)

#Joining of 2 strings
l=['Sudhee','Narayan','Mujumdar','Agadi']
s=';'.join(l)

print(s)

l1=['05','04','2020']
s=':'.join(l1)
print(s)
