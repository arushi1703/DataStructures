def partition(l,k):
    if len(l)<=1:
        return l

    pivot=0
    left=pivot+1
    right=len(l)-1

    while(left<=right):
        while left<len(l) and l[left]<l[pivot]:
            left+=1
        while right>0 and l[right]>l[pivot]:
            right-=1
        if left<=right:
            l[left],l[right]=l[right],l[left]
        else:
            l[pivot],l[right]=l[right],l[pivot]
        
    left_l=l[:right]
    right_l=l[right+1:]

    if len(left_l)>k:
        return partition(left_l,k)
        
    else :
        return left_l+[l[right]]+partition(right_l,k-len(left_l)-1-1)
        

l=[20,12,30,40,5,7,10,19,25,35,45]
print(partition(l,8))
    
    
    
