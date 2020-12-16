a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
c=int(input('Enter third number:'))

x=a if a<b and a<c else (b if b<c else c)
print(x)

y='equal' if a==b else ('smaller' if a<b else 'bigger')
print(y)

