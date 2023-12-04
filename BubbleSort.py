from random import *
from time import *

def BubbleSort(l):
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp

l=[]
for i in range(10):
    x=randint(0,500)
    if x in l:
        continue
    else:
        l.append(x)

print("List:",l)
start=time()
BubbleSort(l)
print("Time taken:",time()-start)
print("sorted list:",l)
