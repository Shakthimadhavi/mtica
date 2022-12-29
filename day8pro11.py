def checkEvenOdd(num1):
    assert(num1>0),"negative numbers"
    if num1%2==0:
        return "Even"
    else:
        return "Odd"

for i in range(3):
    num=int(input("enter a no:"))
    try:
        print(num,"is",checkEvenOdd(num))
    except AssertionError as ob:
        print(ob)
