from random import *
from time import *


def InsertionSort(l):
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while j>=0 and key<l[j]:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=key

l=[]
for i in range(10):
    x=randint(0,500)
    if x in l:
        continue
    else:
        l.append(x)

print("List:",l)
start=time()
InsertionSort(l)
print("Time taken:",time()-start)
print("sorted list:",l)
