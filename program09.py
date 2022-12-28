##lst=[10,15,2,25,30,3,40,4]
##ans=[]
##for i in lst:
 ##   if i*i>50:
##        ans.append(i*i)
##print(ans)

lst=[10,15,2,25,30,3,40,4]
ans=[i*i for i in lst if i*i>50 ]
print(ans)
