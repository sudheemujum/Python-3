#Finding unique vowels

word=input('Enter the any word to search:')
s=set(word)
v={'a','e','i','o','u'}

result=s.intersection(v)

print('The different vowels present in "{}" are:{}'.format(word,result))
