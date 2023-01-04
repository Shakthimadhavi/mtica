x=5;y=7
def changeme( mylist):
    "This function demonstrates local and global variables"
    p=89
    global x,y
    x=y+2
    mylist = [1,2,3,4]
    print("Values inside the function: ", mylist)
    print("local variables are:",locals())
    print("global variables are:",globals())
    return
mylist_var = [10,20,30]
changeme( mylist_var )
print ("Values outside the function: ", mylist_var)
