from random import *
from time import *


def BinarySearch(l,s):
    ll=0
    ul=len(l)-1
    while ll<=ul:
        mid=(ll+ul)//2
        if s==l[mid]:
            return mid
        elif s<l[mid]:
            ul=mid-1
        else:
            ll=mid+1
    return -1

l=[]
for i in range(10):
    x=randint(0,50)
    if x in l:
        continue
    else:
        l.append(x)
        
print("List:",l)
s=int(input("enter search element:"))
start=time()
l.sort()
print("Sorted List:",l)
y=BinarySearch(l,s)
print("Time taken:",time()-start)
if y==-1:
    print("Search element not found.")
else:
    print("Search element found at",y,"position")



    
