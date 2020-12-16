#sets problem with decrease and conquer

def sets_decrease(n):
    if n==0:
        return 1
    else:
        return 2*sets_decrease(n-1)

print(sets_decrease(3))

def sets_divide(n):
    if n==0:
        return 1
    else:
        return sets_decrease(n-1)*sets_decrease(n-1)

print(sets_decrease(4))
