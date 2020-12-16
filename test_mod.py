def merge_sort(arr):
    if len(arr)<=1:
        return arr

    m=len(arr)//2
    L=arr[:m]
    R=arr[m:]

    merge_sort(L)
    merge_sort(R)

    i=j=0

    aux=[]

    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            aux.append=L[i]
            i+=1
        else:
            aux.append=R[j]
            j+=1

    while i<len(L):
        aux.append=L[i]
        i+=1
    while j<len(R):
        aux.append=R[j]
        j+=1

    arr[:]=aux
    return arr

l=[3,1]

print(merge_sort(l))
