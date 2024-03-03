from random import *
def quick_sort(l):
    if (len(l)>1):
        pivot=0
        left=1
        right=len(l)-1

        while(left<=right):
            while(left<len(l) and l[left]<l[pivot]):
                left+=1
            while(right>0 and l[right]>l[pivot]):
                right-=1
            if left<=right:
                l[left],l[right]=l[right],l[left]
            else:
                l[pivot],l[right]=l[right],l[pivot]
        
        left_l=l[:right]
        right_l=l[right+1:]
        quick_sort(left_l)
        quick_sort(right_l)
        l[:]=left_l+[l[right]]+right_l

l=[]
for i in range(10):
    x=randint(0,500)
    if x in l:
        continue
    else:
        l.append(x)

print("Original list: ",l)
quick_sort(l)
print("Sorted list:",l)
