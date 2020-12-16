#List comprehensions

l1=[x for x in range(1,11)]

l2=[2**x for x in range(1,11) if x%2==0]

print(l1)

print(l2)

#create list with elements present in l1 but not in l2

l1=[10,20,30,40,70,50]
l2=[30,40,50,60]

l3=[x for x in l1 if x not in l2]

print(l3)

#create list with elements present in both l1 and l2

l1=[10,20,30,40,70,50]
l2=[30,40,50,60]

l3=[x for x in l1 if x in l2]

print(l3)

l1=['Sudhee','Subbu','Manasa','Mujumdar']

l2=[x[0] for x in l1]

print(l2)

s='the quick brown fox jumps over the lazy dog'

words=s.split()

print(words)

l=[[word.upper(),len(word)] for word in words]

print(l)

#Program to find unique vowels present in the given word

vowels=['a','e','i','o','u']

word=input('Enter the string:')

result=[ch*2+ch for ch in vowels if ch in word]

print(result)
