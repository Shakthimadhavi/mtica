sample_dict = {
    'M':50,
    'physics':82,
    'Math':65,
    'history':75
}
print(min(sample_dict, key=sample_dict.get))
