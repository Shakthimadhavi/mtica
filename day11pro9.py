sample_dict = {
    "name": "kelly",
    "age": 25,
    "salary": 8000,
    "city":"New york"}
keys = ["name","salary"]

for i in keys:
    sample_dict.pop(i)
print(sample_dict)

