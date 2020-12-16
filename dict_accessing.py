d={100:'Sudhee',200:'Mujumdar',300:'Agadi'}

d[500]='Haveri'
d[400]='Karnataka'
d[200]='Mujum'

key=int(input('Enter the key to search:'))

if key in d:
    print('The corresponding value is:',d[key])
else:
    print('Entered value is not in dictionary')

#deleting the item
del d[500],d[100],d[700]

print(d[500])
