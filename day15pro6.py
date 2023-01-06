def findFactor(n):
    temp=list()
    for i in range(1,n+1):
        if n%i==0:
            temp.append(i)
    return temp

def findGCD(n1,n2):
    lstn1=findFactor(n1)
    lstn2=findFactor(n2)
    s1=set(lstn1)
    s2=set(lstn2)
    ans=list(s1.intersection(s2))
    ans.sort()
    return ans[-1]
print("Enter two numbers")
a = int(input())
b = int(input())
print(findGCD(a,b))
