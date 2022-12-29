##num1=int(input("Enter a no:"))
##    print(num1, 'is even')
##if num1%2==1:
##    print(num1,'is odd')
##
##print("we learnt if keyword")

def checkEven(num1):
   # num1=int(input("Enter a no:"))
    if num1%2==0:
       # print(num1, 'is even')
       str1=str(num1)+"is even"
    return str1

def checkOdd(num1):
    #num1=int(input("enter a no:"))
    if num1%2==1:
       # print(num1, 'is odd')
         return "Odd"
    return None

        
checkEven()
checkodd()
