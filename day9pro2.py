def printSeriesIncreasing(ch,n):
    assert isinstance(ch,str),"first argument should be String"
    assert isinstance(n,int),"second argument should be int"
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
try:
    printSeriesdecreasing(inpch,inpNum)
except AssertionError as ob:
    print(ob)
##printSeriesdecreasing(inpch,inpNum)
