def add(n1,n2):
    temp=n1+n2
    global a,b
    a+=10
    print("Output of globals:",globals())
    print("Output of locals:",locals())
    return temp
a=int(input())
b=int(input())
c=add(a,b)
print(a,'+',b,'=',c)
