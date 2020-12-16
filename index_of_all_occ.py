#Print index of all occurences

s='ABCABCCABCXXXABCABCGCABACBABC'

ss=input('Enter sub string to search:')
lss=len(ss)
i=0

while i<=len(s)+1:
    if s.find(ss,i,i+3)!=-1:
        print(s.find(ss,i,i+3))
        i+=3
    else:
        i+=1
print('THE NUMBER OF OCCURENCES:',s.count(ss))

