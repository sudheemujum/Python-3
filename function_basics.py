def sqrit(num):
    sq=num*num
    print('Square of number {} is {}'.format(num,sq))

sqrit(2)
sqrit(4)
sqrit(7)

def add(a,b):
    sum=a+b
    return sum

ret=add(10,20)
print(ret)
print('The sum:',add(100,234))

def test(a,b):
    print('The sum is:',a+b)

ret=test(10,20)
print(ret)

def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    return sum,sub,mul
t=calc(10,20)

print(type(t))
print(t)
print('The results are')
for x in t:
    print(x)
