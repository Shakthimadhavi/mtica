def checkAnagram(s1,s2):
    if sorted(s1)==sorted(s2):
        return'Yes'
    else:
        return'No'
inp=input().split()
print(checkAnagram(inp[0],inp[1]))
