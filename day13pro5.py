def printAdd(a,b):
    return a+b
def printSub(a,b):
    return a-b
def printMult(a,b):
    return a*b
def printDiv(a,b):
    return a/b
def choice():
    print("+:Addition");print("-:Substraction");
    print("*:Multiplication")
    print("/:Division");  print("q:Quit")
    return
ColorSelect={"+":printAdd,"-":printSub,"*":printMult,"/":printDiv}
while True:
    choice()
    selection=input("select a arithmetic operation:")
    if selection=='q' or selection=='Q': break
    if ((selection=='+') or (selection=='-')or
        (selection=='*')or (selection=='/')):
        n1=int(input("Enter first no:"))
        n2=int(input("Enter Second no:"))
        z=ColorSelect[selection](n1,n2)
        print(n1,selection,n2,'=',z)
        
