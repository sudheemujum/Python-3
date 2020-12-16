s=input('Enter some string:')

i=0

for x in s:
    print('The positive index is: {} and negative index is: {} for the character {}'.format(i,i-len(s),x))
    i+=1
    
