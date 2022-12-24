Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'hello'"world"'python'
'helloworldpython'
a="hello""world"'python'
a
'helloworldpython'
a="hello","world",'python'
type(a)
<class 'tuple'>
a=23,7.9,'python',5+8j,'c'
a
(23, 7.9, 'python', (5+8j), 'c')
a=(5)
b=(5.8)
c=('hello')
type(a)
<class 'int'>
a=(5,)
type(a)
<class 'tuple'>
type(b)
<class 'float'>
type(c)
<class 'str'>
type(lst1)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    type(lst1)
NameError: name 'lst1' is not defined
lst1=[15,10]
type(lst1)
<class 'list'>
lst1.append(10)
lst1
[15, 10, 10]
lst1.append(15)
lst1.append(10)
lst1
[15, 10, 10, 15, 10]
lst1.append('python')
lst1
[15, 10, 10, 15, 10, 'python']
lst1.clear()
lst1
[]
lst1=[10,15,10,'python']
lst1.count(10)
2
lst1.count(15)
1
lst1.count(25)
0
lst1.count('python')
1
lst1.count('Python')
0
len(lst1)
4
lst2=lst1
lst1
[10, 15, 10, 'python']
lst2
[10, 15, 10, 'python']
del lst2[-1]
lst2
[10, 15, 10]
lst1
[10, 15, 10]
lst3=lst1.copy()
print(id(lst1),id(lst3))
2952486359744 2952486392384
lst1
[10, 15, 10]
lst3
[10, 15, 10]
lst3.append(10)
lst3.append(10)
lst3
[10, 15, 10, 10, 10]
lst1
[10, 15, 10]
lst4=lst1[:]
print(id(lst1),id(lst4))
2952486359744 2952445631744
lst1
[10, 15, 10]
lst1[:]
[10, 15, 10]
lst1[1:]
[15, 10]
lst1.append([11,22])
lst1
[10, 15, 10, [11, 22]]
lst1[-1]
[11, 22]
lst1.append(('c','c++','java','python'))
lst1
[10, 15, 10, [11, 22], ('c', 'c++', 'java', 'python')]
lst1.append('hello')
lst1
[10, 15, 10, [11, 22], ('c', 'c++', 'java', 'python'), 'hello']
del lst1[3:5]
lst1
[10, 15, 10, 'hello']
lst1.extend([11,22])
lst1
[10, 15, 10, 'hello', 11, 22]
lst1.extend(('c','c++','java','python'))
lst1
[10, 15, 10, 'hello', 11, 22, 'c', 'c++', 'java', 'python']
lst1.index(0)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    lst1.index(0)
ValueError: 0 is not in list
lst1.index('c')
6
lst1.index(10)
0
lst1.index(10,1,9)
2
lst1.index(20)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    lst1.index(20)
ValueError: 20 is not in list
lst1.insert(0,'mca')
lst1
['mca', 10, 15, 10, 'hello', 11, 22, 'c', 'c++', 'java', 'python']
lst1.insert(0,'mca')
lst1
['mca', 'mca', 10, 15, 10, 'hello', 11, 22, 'c', 'c++', 'java', 'python']
lst1.insert(11,'btech')
lst1
['mca', 'mca', 10, 15, 10, 'hello', 11, 22, 'c', 'c++', 'java', 'btech', 'python']
lst1.insert(51,'btechEEE')
lst1
['mca', 'mca', 10, 15, 10, 'hello', 11, 22, 'c', 'c++', 'java', 'btech', 'python', 'btechEEE']
lst1.insert(0,'c')
lst1
['c', 'mca', 'mca', 10, 15, 10, 'hello', 11, 22, 'c', 'c++', 'java', 'btech', 'python', 'btechEEE']
lst1.index('c)
           
SyntaxError: unterminated string literal (detected at line 1)
lst1.index('c')
           
0
lst1.index('c',2)
           
9
lst1.index('c',9)
           
9
lst1.pop()
           
'btechEEE'
lst1
           
['c', 'mca', 'mca', 10, 15, 10, 'hello', 11, 22, 'c', 'c++', 'java', 'btech', 'python']
a=lst1.pop()
           
a
           
'python'
lst1
           
['c', 'mca', 'mca', 10, 15, 10, 'hello', 11, 22, 'c', 'c++', 'java', 'btech']
a=lst1.pop(11)
           
a
           
'java'
a=lst1.pop(1)
           
a
           
'mca'
lst
           
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    lst
NameError: name 'lst' is not defined. Did you mean: 'lst1'?
lst1
           
['c', 'mca', 10, 15, 10, 'hello', 11, 22, 'c', 'c++', 'btech']
a=lst1.pop(4)
           
a
           
10
lst1
           
['c', 'mca', 10, 15, 'hello', 11, 22, 'c', 'c++', 'btech']
b=[]
           
b
           
[]
b.pop()
           
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    b.pop()
IndexError: pop from empty list
lst1
           
['c', 'mca', 10, 15, 'hello', 11, 22, 'c', 'c++', 'btech']
lst1.remove('c')
           
lst1
           
['mca', 10, 15, 'hello', 11, 22, 'c', 'c++', 'btech']
b=lst1.remove(11)
           
b
           
lst1
           
['mca', 10, 15, 'hello', 22, 'c', 'c++', 'btech']
lst1.reverse()
           
lst1
           
['btech', 'c++', 'c', 22, 'hello', 15, 10, 'mca']
L1=[34,21,5.9,89,56,23]
           
L2=['papaya','apple','orange','gua']
           
L1
           
[34, 21, 5.9, 89, 56, 23]
L1.sort()
           
L1
           
[5.9, 21, 23, 34, 56, 89]
L1.sort(reverse=True)
           
L1
           
[89, 56, 34, 23, 21, 5.9]
L2=['papaya','apple','orange','gua']
           
L2.sort()
           
L2
           
['apple', 'gua', 'orange', 'papaya']
L2.sort(reverse=True)
           
L2
           
['papaya', 'orange', 'gua', 'apple']

=================== RESTART: D:/pythonpractice55/day4/program01.py ===================
[[13, 'chinna', 82, 79], [35, 'Kousi', 86, 85], [44, 'Madhavi', 75, 87], [53, 'shakshi', 72, 80]]
[[53, 'shakshi', 72, 80], [44, 'Madhavi', 75, 87], [13, 'chinna', 82, 79], [35, 'Kousi', 86, 85]]
[[13, 'chinna', 82, 79], [53, 'shakshi', 72, 80], [35, 'Kousi', 86, 85], [44, 'Madhavi', 75, 87]]

=================== RESTART: D:/pythonpractice55/day4/program01.py ===================
enter name:student
good morning :student

=================== RESTART: D:/pythonpractice55/day4/program01.py ===================
enter namestudent
good morning student

=================== RESTART: D:/pythonpractice55/day4/program01.py ===================
enter nameStudent
good morning Student

=================== RESTART: D:/pythonpractice55/day4/program02.py ===================
Enter your name:madhavi
Good Morning Madhavi
