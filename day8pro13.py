##def addNumber():
##    num1=int(input("enter a no:"))
##    num2=int(input("enter a no:"))
##    res=num1+num2
##    print(num1,'+',num2,'=',res,sep='')
##    return None
##addNumber()

##def addNumber(num1,num2):
##    res=num1+num2
##    return res
##inp1=int(input("Enter a no:"))
##inp2=int(input("Enter a no:"))
##print(inp1,'+',inp2,'=',addNumber(inp1,inp2),sep='')


def addNumber(num1,num2):
    res=num1+num2
   return res
for i in range(3):
    inp1=int(input("Enter a no:"))
    inp2=int(input("Enter a no:"))
    print(inp1,'+',inp2,'=',addNumber(inp1,inp2),sep='')
