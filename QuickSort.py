from random import *

def quickSort(l):
    if (len(l)<=1):
        return l
    else:
        pivot=l[len(l)//2]
        left=[x for x in l if(x<pivot)]
        middle=[x for x in l if(x==pivot)]
        right=[x for x in l if(x>pivot)]
        return quickSort(left)+middle+quickSort(right)

l=[]
for i in range(10):
    x=randint(0,500)
    if x in l:
        continue
    l.append(x)

print("Original list: ",l)
quickSort(l)
print("Sorted List: ", l)
