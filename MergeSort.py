from random import *

def MergeSort(l):
    if len(l)>1:
        mid=len(l)//2
        lefthalf=l[:mid]
        righthalf=l[mid:]

        MergeSort(lefthalf)
        MergeSort(righthalf)

        i=0
        j=0
        k=0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                l[k]=lefthalf[i]
                i+=1
            else:
                l[k]=righthalf[j]
                j+=1
            k+=1

        while i<len(lefthalf):
            l[k]=lefthalf[i]
            i+=1
            k+=1

        while j<len(righthalf):
            l[k]=righthalf[j]
            j+=1
            k+=1

    return l

l=[]
for i in range(10):
    x=randint(0,500)
    if x in l:
        continue
    else:
        l.append(x)
print("Original List:",l)
print("Sorted List:",MergeSort(l))
