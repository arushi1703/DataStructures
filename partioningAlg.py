def partition(l,k):
    if len(l)<=1:
        return l

    pivot=l[0]
    left=[n for n in l if n<pivot]
    middle=[n for n in l if n==pivot][:-1]
    right=[n for n in l if n>pivot]
    right= middle + right

    if len(left)>k:
        return partition(left,k)
    else:
        return left + [pivot] + middle + partition(right,k-len(left)-1  -len(middle))

k=int(input("Enter value for k:"))
l=[20,12,30,40,5,7,10,19,25,35,45]
print(k," smallest elements: ",partition(l,k)[:k])
