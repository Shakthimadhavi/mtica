lst=[1,2,3,4]
it = iter(lst)
for x in it:
    print(x, end='')
import sys
while True:
    try:
        print(next(it))
    except StopIteration as ob:
        print(ob)
        break
    
