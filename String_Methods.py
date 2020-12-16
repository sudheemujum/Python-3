#String methods
city=input('Enter your sity name:').strip()

if city=='Hyderabad':
    print('City is Hyderabad')
elif city=='Bengaluru':
    print('City is Bengaluru')
else:
    print('Invalid city name')
    print(city)

#Finding substring

s='ABCBE'

print(s.find('B'))
print(s.rfind('b'))

s1='ABCDEFGHIJKLMBN'

print(s1.find('B',3,8))
print(s1.rfind('F',3,8))

#Index method

s2='ABCDBE'
print(s2.index('B'))
#print(s2.index('Z'))


print(s2.rindex('BCD'))
#print(s2.rindex('Z'))

#Count methods

s3='ABCDBEDBDBABBABBBBB'

print('Just count B',s3.count('B'))
print('Just count BB',s3.count('BB'))
print('Count BB in range',s3.count('BB',4,100))


