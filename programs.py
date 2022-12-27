Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================ RESTART: D:/pythonpractice55/day6/program01.py ================
Enter a value(0 to end):5
Enter a value(0 to end):3
Enter a value(0 to end):11
Enter a value(0 to end):0
min: 3
Max: 11
Avg: 6.3

================ RESTART: D:/pythonpractice55/day6/program01.py ================
Enter a value(0 to end):5
Enter a value(0 to end):3
Enter a value(0 to end):11
Enter a value(0 to end):0
min: 3
Max: 11
Avg: 6.3

================ RESTART: D:/pythonpractice55/day6/program01.py ================
Enter a value(0 to end):5
Enter a value(0 to end):3
Enter a value(0 to end):11
Enter a value(0 to end):0
min: 3
Max: 11
Avg: 6.3

========== RESTART: D:/pythonpractice55/day6/program02.py =========
Enter a value(-1 to end):5
Enter a value(-1 to end):12
Enter a value(-1 to end):11
Enter a value(-1 to end):3
Enter a value(-1 to end):8
Enter a value(-1 to end):10
Enter a value(-1 to end):
========== RESTART: D:/pythonpractice55/day6/program02.py =========
Enter a value(-1 to end):5
Enter a value(-1 to end):12
Enter a value(-1 to end):11
Enter a value(-1 to end):3
Enter a value(-1 to end):8
Enter a value(-1 to end):10
Enter a value(-1 to end):-1
Even: 12 8 10
min: 8
max: 12
avg: 10.0
Odd: 5 11 3
min: 3
Traceback (most recent call last):
  File "D:/pythonpractice55/day6/program02.py", line 18, in <module>
    print("Max:",max(lstodd))
NameError: name 'lstodd' is not defined. Did you mean: 'lstOdd'?

========== RESTART: D:/pythonpractice55/day6/program02.py =========
Enter a value(-1 to end):5
Enter a value(-1 to end):12
Enter a value(-1 to end):11
Enter a value(-1 to end):3
Enter a value(-1 to end):8
Enter a value(-1 to end):10
Enter a value(-1 to end):-1
Even: 12 8 10
min: 8
max: 12
avg: 10.0
Odd: 5 11 3
min: 3
Traceback (most recent call last):
  File "D:/pythonpractice55/day6/program02.py", line 18, in <module>
    print("Max:",max(lstodd))
NameError: name 'lstodd' is not defined. Did you mean: 'lstOdd'?

========== RESTART: D:/pythonpractice55/day6/program02.py =========
Enter a value(-1 to end):5
Enter a value(-1 to end):12
Enter a value(-1 to end):11
Enter a value(-1 to end):3
Enter a value(-1 to end):8
Enter a value(-1 to end):10
Enter a value(-1 to end):-1
Even: 12 8 10
min: 8
max: 12
avg: 10.0
Odd: 5 11 3
min: 3
Max: 11
Avg: 6.3

========== RESTART: D:/pythonpractice55/day6/program02.py =========
Enter a value(-1 to end):5
Enter a value(-1 to end):12
Enter a value(-1 to end):11
Enter a value(-1 to end):3
Enter a value(-1 to end):8
Enter a value(-1 to end):10
Enter a value(-1 to end):-1
Even: 12 8 10
min: 8
max: 12
avg: 10.0
Odd: 5 11 3
min: 3
Max: 11
Avg: 6.3

========== RESTART: D:/pythonpractice55/day6/program03.py =========
Enter an integer==>84
84,88

========== RESTART: D:/pythonpractice55/day6/program03.py =========
Enter an integer==>84
84 , 8 8

========== RESTART: D:/pythonpractice55/day6/program03.py =========
Enter an integer==>34
34@,@3@3

========== RESTART: D:/pythonpractice55/day6/program03.py =========
Enter an integer==>54
54#,#5#5
one=2

============= RESTART: D:/pythonpractice55/day6/04.py =============
one: 5
two: -18
3+4
7
print(3+4)
7
x=3+4
print(x)
7
print(x = 3+4)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(x = 3+4)
TypeError: 'x' is an invalid keyword argument for print()
print(x=3,4)
SyntaxError: positional argument follows keyword argument
import math as m
m.sqrt(3)
1.7320508075688772
m.gcd(24,40)
8
from math import *
sqrt(2)
1.4142135623730951
gcd(24,40)
8
from math import sqrt,gcd
sqrt(2)
1.4142135623730951
gcd(24,40)
8

========================== RESTART: Shell =========================
import math
math.sqrt(2)
1.4142135623730951
math.gcd(24,40)
8
m.sqrt(5)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    m.sqrt(5)
NameError: name 'm' is not defined
import math as m
m.sqrt(5)
2.23606797749979
m.trunc(4.5)
4
m.floor(9.8)
9
m.ceil(9.1)
10
m.log(1024,2)
10.0

========================== RESTART: Shell =========================
print('{0},{1},{2}'.format('apple','banana','carrot','pen'))
apple,banana,carrot
print('{0},{1}{0}{0}{3} {2}'.format('apple','banana','carrot','pen'))
apple,bananaappleapplepen carrot
print('{0},{1} {0}{0}{3} {2}'.format('apple','banana','carrot','pen'))
apple,banana appleapplepen carrot
print('{0},{1},{0},{0},{3} {2}'.format('apple','banana','carrot','pen'))
apple,banana,apple,apple,pen carrot
print('{},{},{}'.format('apple','banana','carrot'))
apple,banana,carrot
print('Gangully purchased a kg of {},a dozen of {}and half kg of {}'.format('apple','banana','carrot'))
Gangully purchased a kg of apple,a dozen of bananaand half kg of carrot
print(gangully purchased a kg of {},a dozen of {} and half kg of {}'.format('apple','banana','carrot'))
      
SyntaxError: unterminated string literal (detected at line 1)
print('Gangully purchased a kg of {},a dozen of {}and half kg of {}'.format('apple','banana','carrot'))
      
Gangully purchased a kg of apple,a dozen of bananaand half kg of carrot
print('{2},{1},{0}'.format('apple','banana','carrot'))
      
carrot,banana,apple
print('{2},{1},{1}, {0}'.format('apple','banana','carrot'))
      
carrot,banana,banana, apple
print('{2}, {1}, {0}'.format(*'abcd'))
      
c, b, a
x,*y,z='computer'
      
x
      
'c'
z
      
'r'
y
      
['o', 'm', 'p', 'u', 't', 'e']
print('coordinate:{latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81w'))
      
coordinate:37.24N, -115.81w
print('welcome:{name},your college is: {college}'.format(name='Ganguly, college='MTICA'))
                                                         
SyntaxError: unterminated string literal (detected at line 1)
print('welcome:{name},your college is: {college}'.format(name='Ganguly', college='MTICA'))
                                                         
welcome:Ganguly,your college is: MTICA

=================================== RESTART: Shell ===================================
coord = {3, 5)
                                                         
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
coord = (3, 5)
                                                         
abc=(2, 9)
                                                         
type(coord)
                                                         
<class 'tuple'>
type(abc)
                                                         
<class 'tuple'>
abc[0]
                                                         
2
print('x:{0[0]}; y: {0[1]};{1[1]}'.format(coord,abc))
                                                         
x:3; y: 5;9
