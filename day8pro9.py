##num1=int(input("Enter a no:"))
##    print(num1, 'is even')
##if num1%2==1:
##    print(num1,'is odd')
##
##print("we learnt if keyword")

def checkEven(num1):
    if num1%2==0:
         return "Even"
    return None

def checkOdd(num1):
    if num1%2==1:
        return "Odd"
    return None

num=int(input("enter a no:"))
x=checkEven(num)
y=checkOdd(num)
print("x=",x)
print("y=",y)
print(checkEven(num))
print(checkOdd(num))
