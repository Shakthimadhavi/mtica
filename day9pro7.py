def printDay(dn):
 if(dn==1):
    return "sunday"
 elif(dn==2):
    return "Monday"
 elif(dn==3):
    return "tuesday"
 elif(dn==4):
    return "wednesday"
 elif(dn==5):
     return "thursday"
 elif(dn==6):
     return "friday"
 elif(dn==7):
     return "saturday"
 
 else:
    return "invalid"
for i in range(3):
    inpNum=int(input())
    print(printDay(inpNum))
