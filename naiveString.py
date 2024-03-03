def find(string, pattern):
    if len(string) < len(pattern):
        return "match not found"
    for i in range(len(string)):
        if string[i:i+len(pattern)]==pattern:
            return f"Match found at {i} position"
    return "Match not found"

string="abcdabce"
pattern="bce"
print(find(string,pattern))
