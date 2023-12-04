from random import *
from time import *

def LinearSearch(l,s):
    for i in range(0,len(l)):
        if l[i]==s:
            return i
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
'''l.sort()
print("Sorted List:",l)'''
y=LinearSearch(l,s)
print("Time taken:",time()-start)
if y==-1:
    print("Search element not found.")
else:
    print("Search element found at",y,"position")
