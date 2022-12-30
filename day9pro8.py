def printDay(dn):
 if(dn==1):
    da= "sunday"
 elif(dn==2):
    da= "Monday"
 elif(dn==3):
    da= "tuesday"
 elif(dn==4):
    da= "wednesday"
 elif(dn==5):
     da= "thursday"
 elif(dn==6):
     da= "friday"
 elif(dn==7):
     da= "saturday"
 return da
 
def printDay1(dn):
 if(dn==1):
    da= "sunday"
 if(dn==2):
    da= "Monday"
 if(dn==3):
    da= "tuesday"
 if(dn==4):
    da= "wednesday"
 if(dn==5):
     da= "thursday"
 if(dn==6):
     da= "friday"
 if(dn==7):
     da= "saturday"
 return da

import time 
for i in range(7):
    inpNum=int(input())
    start=time.time()
    print(printDay(inpNum))
    print((time.time()-start)*10000000)
    start=time.time()
    print(printDay1(inpNum))
    print((time.time()-start)*10000000)
