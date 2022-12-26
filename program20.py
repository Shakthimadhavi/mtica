def extract_spchar(s):
    spchar=0
    for i in s:
        if i not in 'AEIOUBCDFGHJKLMNPQRSTVWXYZaeioubcdfgho\
jklmnxzsqwrtypV0123456789':
            spchar+=1
    return spchar

str1=input()
a=extract_spchar(str1)
print("no of special character in:'",str1,"' is",a)
