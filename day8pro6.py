num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
try:
    res=num1/num2
except ZeroDivisionError:
    print("Division by Zero not allowed")
else:
    print (num1, '/' ,num2, '=', res)
print('Thanks')
    
    
