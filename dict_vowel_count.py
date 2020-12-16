word=input('Enter the string to find the vowels:')
vowels={'a','e','i','o','u'}

d={}

for ch in word:
    if ch in vowels:
        d[ch]=d.get(ch,0)+1
for k,v in sorted(d.items()):
    print('Vowel {} is appearing {} times'.format(k,v))
