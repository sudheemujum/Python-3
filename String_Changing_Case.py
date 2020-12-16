#Changing case of characters

s='sudheendra MUJAMADAR Agadi haveRI'

print(s.upper())

print(s.lower())

print(s.swapcase())

print(s.title())

print(s.capitalize())

s2='SUDHEENDRA Mujamadar AGadi haveRI'

if s.upper()==s2.upper():
    print('Both the strings are same')
else:
    print('Both strings are not same')

s3='suDHee'

print(s3[0].upper()+s3[1:-2].lower()+s3[-1].upper())

    
