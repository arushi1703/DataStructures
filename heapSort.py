from random import *
import heapq

def heapSort(l):
    l2=[]
    for i in range(len(l)):
        heapq._heapify_max(l)
        print(l)
        l[-1],l[0]=l[0],l[-1]
        print(l)
        l2.insert(0,l[-1])
        del l[-1]
    return l2

l=[5,10,15,2,4]

print("Original list: ",l)
print("Sorted List: ",heapSort(l))

