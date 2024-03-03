def find(string, pattern):
    if len(string)<len(pattern):
        return "match not found"
    psum= sum([ord(char)-96 for char in pattern])
    csum= sum([ord(char)-96 for char in string[0:len(pattern)]])
    
    for i in range(0, len(string)-len(pattern)+1):
        if i!=0:
            csum= csum+ ord(string[i+len(pattern)-1])-96
        current=string[i:i+len(pattern)]
        if csum==psum:
            if check(current, pattern):
                return f"Match found at index {i}"
        csum= csum-ord(string[i])+96
    return "Match not found"

def check(str1, str2):
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            return False
    return True

string="ccaccaaedba"
pattern="dba"
print(find(string, pattern))
