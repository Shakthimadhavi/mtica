from math import sqrt
def checkPrime(n):
    if n==1 or n==2 or n==3:
        return n
    for i in range(2,int(sqrt(n))+1):
        if n%i ==0:
            return None
    return n
def findPrimeFactor(n):
    temp=[]
    for i in range(1,n+1):
        if n%i==0:
            if checkPrime(i):
                temp.append(i)
    return temp

a = int(input())
print(*findPrimeFactor(a))
