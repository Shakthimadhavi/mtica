sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print("200 present in a dict")

for k,v in sample_dict.items():
    if v==200:
        print("for",v,"key is",k)
    
