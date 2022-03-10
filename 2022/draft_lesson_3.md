```python
a=3
b=5
```


```python
l = [4,5,6,5,5,4,3,5,6,7,8,7]
```


```python
l[1]
```




    5




```python
l[0]
```




    4




```python
s = 'Alex'
```


```python
s[1]
```




    'l'




```python
s[0]
```




    'A'




```python
l = [4,5,6,7,8,9,]
```


```python
l = [4,5,6,7,8,9]
```


```python
l = [
    4,
    5,
    6,
    7,
    8,
    9,
]
```


```python
l[-1]
```




    9




```python
l[-2]
```




    8




```python
s = 'abcdefghijk'
```


```python
s[1:4]
```




    'bcd'




```python
l
```




    [4, 5, 6, 7, 8, 9]




```python
l[1:4]
```




    [5, 6, 7]




```python
l[1:6:2]
```




    [5, 7, 9]




```python
l[-1:0:-2] # slicing
```




    [9, 7, 5]




```python
1
2
3
4
5
5 6
6
7
8


```


      File "<ipython-input-25-866d4248fcc1>", line 6
        5 6
          ^
    SyntaxError: invalid syntax




```python
s[100]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-27-2a138df92e52> in <module>
    ----> 1 s[100]
    

    IndexError: string index out of range



```python
l
```




    [4, 5, 6, 7, 8, 9]




```python
l[100]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-29-e2a0c2623844> in <module>
    ----> 1 l[100]
    

    IndexError: list index out of range



```python
s
```




    'abcdefghijk'




```python
s[0:100000:2]
```




    'acegik'




```python
l[0:100000:2]
```




    [4, 6, 8]




```python
len(s)
```




    11




```python
len(l)
```




    6




```python
len('')
```




    0




```python
len([])
```




    0




```python
def f(x):
    return x+1
```


```python
l = [1,1,2,34.23, True, False, 'adfasdf', None, f]
```


```python
l[-1](5)
```




    6




```python
l = [ [1,2,3], [7,8,9] ]
```


```python
len(l)
```




    2




```python

```


```python
len(l[0])
```




    3




```python
l = [[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]
```


```python
len(l)
```




    1




```python
len([ [], [], []  ])
```




    3




```python
a = [1,2,3]
```


```python
a = [5,6,a]
```


```python
a
```




    [5, 6, [1, 2, 3]]




```python
[a, [a,a, [a]]]
```




    [[5, 6, [1, 2, 3]],
     [[5, 6, [1, 2, 3]], [5, 6, [1, 2, 3]], [[5, 6, [1, 2, 3]]]]]




```python
l = [5,6,7,8,9]
```


```python
5 in l
```




    True




```python
'mitsos' in l
```




    False




```python
[5,6] in [5,6]
```




    False




```python
[5,6] in [5,6,[5,6]]
```




    True




```python
'l' in 'Alex'
```




    True




```python
'lex' in 'Alex'
```




    True




```python
'fdwdf' in 'Alex'
```




    False




```python
'abcdefg'.index('e')
```




    4




```python
[1,2,3,4,5].index(5)
```




    4




```python
'askjfghaljerfghalejgfalejhfgaekjhfgaekjrhfg'.count('g')
```




    6




```python
[1,2,3,4,3,2,3,4,5].count(1)
```




    1




```python
[4,5,6,7,8].find(7)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-65-041512efb010> in <module>
    ----> 1 [4,5,6,7,8].find(7)
    

    AttributeError: 'list' object has no attribute 'find'



```python
'gfdsdfghgf'.find('g')
```




    0




```python
'sdfghjhgfd'.find('g')
```




    3




```python
'sdfghjhgfd'.index('g')
```




    3




```python
'sdfghjhgfd'.index('z')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-69-ff69278f61c8> in <module>
    ----> 1 'sdfghjhgfd'.index('z')
    

    ValueError: substring not found



```python
'sdfghjhgfd'.find('z')
```




    -1




```python
[4,5,6,7,8].index(9)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-71-3f3c9233de30> in <module>
    ----> 1 [4,5,6,7,8].index(9)
    

    ValueError: 9 is not in list



```python
[4,5,6,7,]
```




    [4, 5, 6, 7]




```python
'asdfgdsa' + 'gdhfjkdshagfsdfgb'
```




    'asdfgdsagdhfjkdshagfsdfgb'




```python
[1,2,3] + [7,8,9]
```




    [1, 2, 3, 7, 8, 9]




```python
[1,2,3] * [7,8,9]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-75-7965657d1c01> in <module>
    ----> 1 [1,2,3] * [7,8,9]
    

    TypeError: can't multiply sequence by non-int of type 'list'



```python
[1,2,3] * 7
```




    [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]




```python
['a', 'b', 'c'] * 4
```




    ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']




```python
'abcd' + 'e'
```




    'abcde'




```python
7+5
```




    12




```python
a=7
a += 5
a
```




    12




```python
s = 'abcd'
s += 'e'
s
```




    'abcde'




```python
l = [3,4,5,6,]
l += [7]
l
```




    [3, 4, 5, 6, 7]




```python

```


```python
[3,4,5,6,] + [7]
```




    [3, 4, 5, 6, 7]




```python
l = [1,2,3,4,5]
```


```python
(l[::-1] + [0])[::-1]# ^%$#@#$%^%$#@
```




    [0, 1, 2, 3, 4, 5]




```python
l = [0] + l
```


```python
l
```




    [0, 1, 2, 3, 4, 5]




```python
l
```




    [0, 1, 2, 3, 4, 5]




```python
l = l[:3] + ['mitsos'] + l[3:]
```


```python
l
```




    [0, 1, 2, 'mitsos', 3, 4, 5]




```python
l
```




    [0, 1, 2, 'mitsos', 3, 4, 5]




```python
l[:3] + l[4:]
```




    [0, 1, 2, 3, 4, 5]




```python
l = [1,2,3,4,5]
```


```python
l.insert('mitsos', 2)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-108-8252445c3c18> in <module>
    ----> 1 l.insert('mitsos', 2)
    

    TypeError: 'str' object cannot be interpreted as an integer



```python
help(l.insert)
```

    Help on built-in function insert:
    
    insert(index, object, /) method of builtins.list instance
        Insert object before index.
    



```python
l.insert(2, 'mitsos')
```


```python
l
```




    [1, 2, 'mitsos', 3, 4, 5]




```python
a=3
```


```python
a
```




    3




```python
del a
```


```python
a
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-117-3f786850e387> in <module>
    ----> 1 a
    

    NameError: name 'a' is not defined



```python
l
```




    [1, 2, 'mitsos', 3, 4, 5]




```python
del l[2]
```


```python
l
```




    [1, 2, 3, 4, 5]




```python
l
```




    [1, 2, 3, 4, 5]




```python
l.remove(2)
```


```python
l
```




    [1, 3, 4, 5]




```python
l = [1, 2, 3, 'mitsos', 4, 5]
l
```




    [1, 2, 3, 'mitsos', 4, 5]




```python
l.remove('mitsos')
```


```python
l
```




    [1, 2, 3, 4, 5]




```python
l.append('mitsos')
```


```python
l
```




    [1, 2, 3, 4, 5, 'mitsos']




```python
l = [1,2,3,4,5]
```


```python
l.append([7,8,9]) * 2
len(l)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-146-a06facda6fbb> in <module>
    ----> 1 l.append([7,8,9]) * 2
          2 len(l)


    TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'



```python
b = l.append('mitsos')
```


```python
print(b)
```

    None



```python
None * 2
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-145-60f90da77edb> in <module>
    ----> 1 None * 2
    

    TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'



```python
l = [4,5,6]
l.append([7,8,9])

```


```python
l
```




    [4, 5, 6, [7, 8, 9]]




```python
l = [4,5,6]
l.extend([7,8,9])
l
```




    [4, 5, 6, 7, 8, 9]




```python
'aaaa'  'bbbb'
```




    'aaaabbbb'




```python
a = [
    'abc',
    'def'
    'ghi',
]
```


```python
a
```




    ['abc', 'defghi']




```python
int('34567')
```




    34567




```python
str(65434567)
```




    '65434567'




```python
bool('sasds')
```




    True




```python
list('fghjkjhgfdfghjkjhgfd')
```




    ['f',
     'g',
     'h',
     'j',
     'k',
     'j',
     'h',
     'g',
     'f',
     'd',
     'f',
     'g',
     'h',
     'j',
     'k',
     'j',
     'h',
     'g',
     'f',
     'd']




```python
list('h')
```




    ['h']




```python
list(7) # [7]
```


```python
l = ['a', 'b', 'c']
```


```python
list('abc')
```




    ['a', 'b', 'c']




```python
l
```




    ['a', 'b', 'c']




```python
'<-->'.join(l)
```




    'a<-->b<-->c'




```python
'+'.join(l)
```




    'a+b+c'




```python
' mitsos '.join(l)
```




    'a mitsos b mitsos c'




```python
''.join(l)
```




    'abc'




```python
l
```




    ['a', 'b', 'c']




```python
# askish 5678
def f(x):
    return x+1
```


```python
l = [4,5,6,7,8]
```


```python
l + 10
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-177-ff865001d10f> in <module>
    ----> 1 l + 10
    

    TypeError: can only concatenate list (not "int") to list



```python
def f(x):
    return x+10
```


```python
l
```




    [4, 5, 6, 7, 8]




```python
f(4)
```




    14




```python
list(map(f, l))
```




    [14, 15, 16, 17, 18]




```python
map(f, l)
```




    <map at 0x7f8ed85866a0>




```python
list(map(f, l))
```




    [14, 15, 16, 17, 18]




```python
list(map(f,map(f, l)))
```




    [24, 25, 26, 27, 28]




```python
def f(x):
    return x + ' hello'
```


```python
list(map(f, ['a', 'b', 'c']))
```




    ['a hello', 'b hello', 'c hello']




```python
def f(x):
    return x + 1
```


```python
f(3)
```




    4




```python
l= [10, 20, 30]
```


```python
f(l[0])
```




    11




```python
f((l[1]))
```




    21




```python
f(l[2])
```




    31




```python
new_list= [f(l[0]), f(l[1]), f(l[2])]
new_list
```




    [11, 21, 31]




```python
new_list = list(map(f, l))
new_list
```




    [11, 21, 31]




```python
l = [3,4,5,6,7,8,9,]
```


```python
def g(x):
    return x>5.5
```


```python
def f(x):
    return x + 1
```


```python
g(8)
```




    True




```python
list(filter(g, l))
```




    [6, 7, 8, 9]




```python
l
```




    [3, 4, 5, 6, 7, 8, 9]




```python
list(filter(g,map(f, l)))
```




    [6, 7, 8, 9, 10]




```python
l = [4,5,6,7,8]
```


```python
l
```




    [4, 5, 6, 7, 8]




```python
sum(l)
```




    30




```python
min(l)
```




    [1, 'alex']




```python

```


```python
max(l)
```




    8




```python
l = [ [3,'mitsos'], [1, 'helen'], [2, 'alex'] ]
#l = [ [3,'mitsos'], ['alex', 1], [2, 'helen'] ]
```


```python
min(l)
```




    [1, 'helen']




```python
l = [ [3,'mitsos'], [1, 'helen'], [1, 'alex'] ]
```


```python
min(l)
```




    [1, 'alex']




```python
'alex' < '1'
```




    False




```python
l = [ [3,'mitsos'], [1, 'helen'], [1, 'alex'] ]

```


```python
min(l)
```




    [1, 'alex']




```python
min([1,2,3,2,1,2,3,1,1,1,1,1,1])
```




    1




```python
min([3,3,3,3,3,3])
```




    3




```python
l = [ [3,'mitsos'], [1, 'helen'], [1, 'helen'] ]
min(l)
```




    [1, 'helen']




```python
[1] < [1,'alex']
```




    True




```python
l = [ [3,'mitsos'], [1, 'helen'], [2, 'alex'] ]
min(l)
```




    [1, 'helen']




```python
def f(x):
    #return x[::-1]
    return [x[1], x[0]]
```


```python
list(map(f, l))
```




    [['mitsos', 3], ['helen', 1], ['alex', 2]]




```python
min(map(f, l))
```




    ['alex', 2]




```python
f(min(map(f, l)))
```




    [2, 'alex']




```python
min(l, key=f)
```




    [2, 'alex']




```python
l = ['Athens', 'Heraklion', 'Patras']
```


```python
min(l)
```




    'Athens'




```python
def f(x):
    return x[1]
```


```python
min(l, key=f)
```




    'Patras'




```python
l
```




    ['Athens', 'Heraklion', 'Patras']




```python
sorted(l)
```




    ['Athens', 'Heraklion', 'Patras']




```python
sorted([5,4,5,6,7,6,5,4,3,2])
```




    [2, 3, 4, 4, 5, 5, 5, 6, 6, 7]




```python
sorted([5,4,5,6,7,6,5,4,3,2], reverse=True)
```




    [7, 6, 6, 5, 5, 5, 4, 4, 3, 2]




```python
sorted(l, key=f)
```




    ['Patras', 'Heraklion', 'Athens']




```python
sorted(l, key=f, reverse=True)
```




    ['Athens', 'Heraklion', 'Patras']




```python
l = [['mitsos', 3], ['helen', 1], ['alex', 2]]
sorted(l)
```




    [['alex', 2], ['helen', 1], ['mitsos', 3]]




```python
def f(x):
    return x[1]
```


```python
sorted(l, key=f)
```




    [['helen', 1], ['alex', 2], ['mitsos', 3]]




```python
f('dsafsdf')
```




    's'




```python
f(['asda', 1000])
```




    1000




```python
l
```




    [['mitsos', 3], ['helen', 1], ['alex', 2]]




```python
sorted(l)
l
```




    [['mitsos', 3], ['helen', 1], ['alex', 2]]




```python
l = [5,4,5,4,3,4,5,6,7]
k = sorted(l)
l
```




    [5, 4, 5, 4, 3, 4, 5, 6, 7]




```python
l
```




    [5, 4, 5, 4, 3, 4, 5, 6, 7]




```python
k
```




    [3, 4, 4, 4, 5, 5, 5, 6, 7]




```python
l.sort()
l
```




    [3, 4, 4, 4, 5, 5, 5, 6, 7]




```python
list(range(10, 20))
```




    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]




```python
list(range(10, 20, 2))
```




    [10, 12, 14, 16, 18]




```python
list(range(20, 10, -2))
```




    [20, 18, 16, 14, 12]




```python
list(range(10)) # list(range(0,10))
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
l= ['alex', 'helen', 'kostas']
```


```python
list(enumerate(l))
```




    [(0, 'alex'), (1, 'helen'), (2, 'kostas')]




```python
    
```
