##dict1={"sedan": 1500, "SVU": 2000, "pickup": 2500, "minivan": 1600, "van": 2400, "semi": 13600, "bicycle": 7, "Motorcycle": 110}
##ans=[]
##for i in dict1:
##      if dict1[i]<5000:
##        ans.append(i.upper())
##print(ans)

dict1={"sedan": 1500, "SVU": 2000, "pickup": 2500, "minivan": 1600, "van": 2400, "semi": 13600, "bicycle": 7, "Motorcycle": 110}
ans=[i.upper() for i in dict1 if dict1[i]<5000 ]
print(ans)
