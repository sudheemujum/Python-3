d=eval(input('Enter any dictionary values:'))

sum1=0
for item in d.items():
    sum1=sum1+item[1]
print('Sum of the values:',sum1)

print('Sum of values using sum function:',sum(d.values()))

