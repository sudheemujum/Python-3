a,b,c,d=10,20,30,40

print(a,b,c)
print(a,b,c,sep=':')
print(a,b,c,sep='')

print('Sudheendra',end='::')
print('Mujumdar')
print('Plano',end='$$$')
print('Texas')

print('Combining separator and end statement')
print(a,b,c,sep='**',end='$$')
print(40,50,60,sep='--',end='%%')
print(70,80)
print(90,100)

print('Sudheendra'+'Mujumdar')
print('Sudheendra','Mujumdar')
print('Sudheendra','Mujumdar',sep=':')

print('Replacement operator')
name='Sudheendra'
city='Plano'
salary=1000

print('Hello {}, is living in {} and has salary of {}'.format(name,city,salary))
print('Hello {0}, is living in {1} and has salary of {2}'.format(name,city,salary))
print('Hello {n}, is living in {c} and has salary of {s}'.format(n=name,c=city,s=salary))

print('a={},b={},c={},d={}'.format(a,b,c,d))

print("Formatted string operator")
price=70.56789

print("Price of {}'s car is {}".format(name,price))
print("Price of %s's car is %f" %(name,price))
print("Price of %s's car is %.2f" %(name,price))



