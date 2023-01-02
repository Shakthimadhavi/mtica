sample_dict = {
    "name": "kelly",
    "age": 25,
    "salary": 8000,
    "city":"New york"}
keys = ["name","salary"]
newDict = {}
for i in keys:
    newDict[i]=sample_dict[i]
print(newDict)

newDict={ i:sample_dict[i] for i in keys }
print(newDict)
