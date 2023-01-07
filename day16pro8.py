from itertools import permutations
words = [''.join(p) for p in permutations('yup')]
print(words)
