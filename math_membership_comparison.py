#Mathmatical operators
s1='Sudheendra'
s2='Mujumdar'
s='Agadi Mujumdar'
subs='agadi'

#Membership operators
print(s1+' '+s2)
print(s1*3)

if subs in s:
    print('Substring is present in main string')
else:
    print('Substring is not present in main string')

#Comparison operators

print(ord('s'))
print(chr(45))

firsts='ramya'
seconds='ramba'

if firsts==seconds:
    print('Both first and second string are same')
elif firsts<seconds:
    print('Firsts is lesser than second string')
else:
    print('Second String is lesser than second string')
    for x in seconds:
        print(ord(x),end=';')
    for y in firsts:
        print(ord(y),end=';')



