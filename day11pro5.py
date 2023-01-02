##keys = ['Ten', 'Twenty', 'Thirty']
##values = [10, 20, 30]
##d=dict()
##for i,j in zip(keys,values):
##    d[i]=j
##
##print(d)

##dict1 = {'Ten': 10,'Twenty': 20,'thirty': 30}
##dict2 = {'Thirty': 30,'Fourty': 40,'Fifty': 50}
##dict3={**dict1,**dict2}
##print(dict3)
##

dict1 = {'Ten': 10,'Twenty': 20,'thirty': 30}
dict2 = {'Thirty': 30,'Fourty': 40,'Fifty': 50}
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)
print(dict3)
