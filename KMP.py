def LPS(pattern):
    global lps
    copy=""
    count=0
    for i in pattern:
        if i not in copy:
            count=0
            lps.append(count)
        else:
            count+=1
            lps.append(count)
        copy+=i

def find(string,pattern):
    print(lps)
    flag=0
    if len(string)<len(pattern):
        return "Match not found"
    i=0
    j=-1
    while i<len(string):
        if string[i]==pattern[j+1]:
           i+=1
           j+=1
        else:
            j=lps[j-1]
            if j==0:
                i+=1

        if(j==len(pattern)-1):
            flag=1
            break
    if(flag==1):
        return f"Match found at {i-j} position"
    return "Match not found"

string="ababcabcabababd"
pattern="ababd"
lps=[]
LPS(pattern)
print(find(string, pattern))
