##ans=[]
##for i in range(100,111):
##  temp=[]
##    for j in range(1,10):
##        if i%j==0:
##            temp.append(j)
##  ans.append([i,max(temp)])
##print(ans)

##ans=[]
##for i in range(100,111):
##    ans.append([i,max([ j for j in range(1,11)if i%j==0 ])])
##print(ans)

ans=[ [i,max([ j for j in range(1,11)if i%j==0])]
      for i in range(100,110)]
print(ans)
