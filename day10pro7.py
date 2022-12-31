fo=open(r"D:\pythonpractice55\day10\day10day10\day10a.txt","a")
for i in range(5):
    inpstr=input("Enter string:")
    fo.write(inpstr+'\n')
fo.close()
print("Written to file")
