def extract_vowel(s):
    temp_vowel=''
    for i in s:
        if i in 'AEIOUaeiou':
            temp_vowel+=i
    return temp_vowel
str1=input()
a=extract_vowel(str1)
print("vowels:",a)
