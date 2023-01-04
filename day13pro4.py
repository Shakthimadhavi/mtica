def printJan():
    print('January')
    return
def printFeb():
    print('Febuary')
def printMar():
    print('March')
def printApr():
    print('April')
def printMay():
    print('May')
def printJune():
    print('June')
def printJuly():
    print('July')
def printAug():
    print('August')
def printSep():
    print('September')
def printOct():
    print('October')
def printNov():
    print('November')
def printDec():
    print('December')
def choice():
    print("0:Jan")
    print("1:Feb")
    print("2:Mar")
    print("3:Apr")
    print("4:May")
    print("5:June")
    print("6:July")
    print("7:Aug")
    print("8:Sep")
    print("9:Oct")
    print("10:Nov")
    print("11:Dec")
    return
MonthSelect={0:printJan,1:printFeb,2:printMar,3:printApr,4:printMay,5:printJune,
           6:printJuly,7:printAug,8:printSep,9:printOct,10:printNov,11:printDec}
selection=0
while True:
    if selection == 12:break
    choice()
    selection=int(input("select a Month option:"))
    if (selection>=0) and (selection<7):
        MonthSelect[selection]()
