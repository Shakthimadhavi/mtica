def printSeriesIncreasing(ch,n):
    for i in range(1,n+1,1):
        print(ch*i)
    return None
def printSeriesdecreasing(ch,n):
    for i in range(n,0,-1):
        print(ch*i)
    return None
inpch=input("enter a character:")
inpNum=int(input("enter a no:"))
printSeriesIncreasing(inpch,inpNum)
print('_'*40)
printSeriesdecreasing(inpch,inpNum)
