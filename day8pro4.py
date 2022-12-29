def div(a,b):
    assert (b!=0),"Division by Zero is not defined "
    return a/b

try:
    print (div(55,0))
except AssertionError as ob:
    print(ob)
try:
     print (div(20,3))
except AssertionError as ob:
    print(ob)
try:
     print (div(100,20))
except AssertionError as ob:
    print(ob)

    
    
