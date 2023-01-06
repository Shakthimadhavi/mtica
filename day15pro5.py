def findFactor(n):
    temp=list()
    for i in range(1,n+1):
        if n%i==0:
            temp.append(i)
    return temp
a = int(input())
print(*findFactor(a))
      
