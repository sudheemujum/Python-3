d={100:'A',200:'A',300:'A',400:'D'}

key=int(input('Enter key to get value:'))

if key in d:
    print('The corresponding value is:', d.get(key),d[key])
else:
    print('Entered key is not available')

value=input('Enter the values to get key:')

available=False

for k,v in d.items():
    if v==value:
        print('The corresponding key is:',k)
        available=True
if available==False:
    print('Entered value is not available')

    
