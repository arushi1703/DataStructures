from random import *
from time import *

def SelectionSort(l):
    for i in range (len(l)):
        min_index=i
        for j in range(i+1,len(l)):
            if l[j]<l[min_index]:
                min_index=j
        l[i],l[min_index]=l[min_index],l[i]


l=[]
for i in range(10):
    x=randint(0,500)
    if x in l:
        continue
    else:
        l.append(x)

print("List:",l)
start=time()
SelectionSort(l)
print("Time taken:",time()-start)
print("sorted list:",l)
