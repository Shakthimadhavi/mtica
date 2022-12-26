def count_spchar(s):
    spchar=0
    for i in s:
        if i not in 'AEIOUBCDFGHJKLMNPQRSTVWXYZaeioubcdfghojklmnxzsqwrtypV':
            spchar+=1
    return spchar

str1=input()
a=count_spchar(str1)
print("no of special character in:'",str1,"' is",a)
