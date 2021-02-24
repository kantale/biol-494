```python
def f(x):
    return x+1

def g(x):
    return x-1

f(g(1)+g(2)) + g(f(1)+f(2))
```




    6




```python
a = [4,3,2,5,6,7]
```


```python
a[0]
```




    4




```python
a[1]
```




    3




```python
a[0] = -17
```


```python
a
```




    [-17, 3, 2, 5, 6, 7]




```python
b = "Mitsos"
b[0]
```




    'M'




```python
b[0] = 'L'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-6-78ea47601bd4> in <module>
    ----> 1 b[0] = 'L'
    

    TypeError: 'str' object does not support item assignment



```python
b
```




    'Mitsos'




```python
len(b)
```




    6




```python
len(a)
```




    6




```python
a
```




    [-17, 3, 2, 5, 6, 7]




```python
'Thessaloniki'.count('s')
```




    2




```python
'Thessaloniki'.count('l')
```




    1




```python
'Thessaloniki'.count('q')
```




    0




```python
a
```




    [-17, 3, 2, 5, 6, 7]




```python
a.count(3)
```




    1




```python
'Thessaloniki'.index('s')
```




    3




```python
a
```




    [-17, 3, 2, 5, 6, 7]




```python
a.index(6)
```




    4




```python
a.count("mitsos")
```




    0




```python
a.index(9)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-24-8ab34ac345ab> in <module>
    ----> 1 a.index(9)
    

    ValueError: 9 is not in list



```python
"sadfas".index('q')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-25-9ca0a27640d9> in <module>
    ----> 1 "sadfas".index('q')
    

    ValueError: substring not found



```python
'it' in 'Mitsos'
```




    True




```python
'io' in 'Mitsos'
```




    False




```python
3 in [3,4,5]
```




    True




```python
7 in [3,4,5]
```




    False




```python
a
```




    [-17, 3, 2, 5, 6, 7]




```python
a[0]
```




    -17




```python
a[1]
```




    3




```python
a.count(1)
```




    0




```python
a
```




    [-17, 3, 2, 5, 6, 7]




```python
'abcdefghijklmnop'[2:7:2]
```




    'ceg'




```python
a = [1,2,3,4,5,6,7,8,9]
```


```python
a[2:7:2]
```




    [3, 5, 7]




```python
a[7:2:-1]
```




    [8, 7, 6, 5, 4]




```python
a[7:2:-2]
```




    [8, 6, 4]




```python
a
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
a[-1]
```




    9




```python
a[-2]
```




    8




```python
a[:4]
```




    [1, 2, 3, 4]




```python
a
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
a = [1,2,'mitsos', 4,5]
```


```python
a = [1,2,'mitsos', 4,5, True, False, None, 3+4j]
```


```python
a.index(False)
```




    6




```python
type(a)
```




    list




```python
a = [1,2,3, [7,8,9], True]
```


```python
len(a)
```




    5




```python
a[3]
```




    [7, 8, 9]




```python
a = [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
```


```python
len(a)
```




    1




```python
len([])
```




    0




```python
a= []
```


```python
len(a)
```




    0




```python
len('')
```




    0




```python
a = [  []   ]
```


```python
len(a)
```




    1




```python
a[0]
```




    []




```python
[1,2, [], 5,6]
```




    [1, 2, [], 5, 6]




```python
if 'mitsos':
    print ('hello')
```

    hello



```python
if '':
    print ('hello')
```


```python
if [1,2,3]:
    print ('hello')
```

    hello



```python
if []:
    print ('hello')
```


```python
a = [6,7,8]
```


```python
"mitsos" + "kostas"
```




    'mitsoskostas'




```python
[6,7,8] + [9,10,10]
```




    [6, 7, 8, 9, 10, 10]




```python
"mitsos " * 10
```




    'mitsos mitsos mitsos mitsos mitsos mitsos mitsos mitsos mitsos mitsos '




```python
[1,2,3] * 5
```




    [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]




```python
a=[1,2,3]
```


```python
a = a + [4]
```


```python
a = [1,2,3] + [4]
```


```python
a
```




    [1, 2, 3, 4]




```python
a = a + [10]
```


```python
a
```




    [1, 2, 3, 4, 10]




```python
b = 5
#b = b + 1
b += 1
```


```python
b
```




    6




```python
a = [1,2,3]
#a = a + [4]
a += [4]
print (a)
```

    [1, 2, 3, 4]



```python
a = ["mitsos"] + a
print (a)
```

    ['mitsos', 1, 2, 3, 4]



```python
a += [4] # a = a + [4]
```


```python
a
```




    ['mitsos', 1, 2, 3, 4, 4]




```python
a.append(10)
```


```python
a
```




    ['mitsos', 1, 2, 3, 4, 4, 10]




```python
a
```




    ['mitsos', 1, 2, 3, 4, 4, 10]




```python
a.append([10,9])
```


```python
print(a)
```

    ['mitsos', 1, 2, 3, 4, 4, 10, [10, 9]]



```python
a.extend([10,9])
```


```python
a
```




    ['mitsos', 1, 2, 3, 4, 4, 10, [10, 9], 10, 9]




```python
# a.append(x)
# a += [x]

# a.extend(x)
# a += x

```


```python
a = [1,2,3,4,5]
```


```python
a = ['mitsos'] + a
print (a)
```

    ['mitsos', 1, 2, 3, 4, 5]



```python
a = [1,2,3,4,5]
```


```python
a
```




    [1, 2, 3, 4, 5]




```python
a[:2]
```




    [1, 2]




```python
a[2:]
```




    [3, 4, 5]




```python
['Mitsos']
```




    ['Mitsos']




```python
a = a[:2] + ['Mitsos'] + a[2:]
a
```




    [1, 2, 'Mitsos', 3, 4, 5]




```python
a = [1,2,3,4,5]
a
```




    [1, 2, 3, 4, 5]




```python
a.insert(2, "mitsos")
print (a)
```

    [1, 2, 'mitsos', 3, 4, 5]



```python
a = [1,2,3,4,5]
a.insert(0, 'mitsos')
print (a)
```

    ['mitsos', 1, 2, 3, 4, 5]



```python
a = [1,2,3,4,5]
a.insert(1000, 'Mitsos')
```


```python
a
```




    [1, 2, 3, 4, 5, 'Mitsos']




```python
a
```




    [1, 2, 3, 4, 5, 'Mitsos']




```python
a[:2]
```




    [1, 2]




```python
a[3:]
```




    [4, 5, 'Mitsos']




```python
a = a[:2] + a[3:]
a
```




    [1, 2, 4, 5, 'Mitsos']




```python
a = [1, 2, 3, 4, 5]
print (a)
```

    [1, 2, 3, 4, 5]



```python
a[:2] + a[3:]
```




    [1, 2, 4, 5]




```python
del a[2]
print (a)
```

    [1, 2, 4, 5]



```python
b = 3
print (b)
```

    3



```python
del b
```


```python
print(b)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-125-67e500defa1b> in <module>
    ----> 1 print(b)
    

    NameError: name 'b' is not defined



```python
a
```




    [1, 2, 4, 5]




```python
a[::-1]
```




    [5, 4, 2, 1]




```python
a = [1,2,3,4,5,6,7]
```


```python
[1,2,3,4,5,6,7, 5+3, ]
```




    [1, 2, 3, 4, 5, 6, 7, 8]




```python
def f(x):
    return x[2]

f([4,5,6])
```




    6




```python
def f(x):
    return x+1
```


```python
a=[1,2,3]
```


```python
type(f)
```




    function




```python
a.insert(2,f)
```


```python
a
```




    [1, 2, <function __main__.f(x)>, 3]




```python
a[2](10)
```




    11




```python
b=f
```


```python
f(3)
```




    4




```python
b(3)
```




    4




```python
def f(a,b):
    return a+b
```


```python
def g(a,b):
    return a-b
```


```python
l = [f,g]
```


```python
l[0](4,5)
```




    9




```python
l[1](4,5)
```




    -1




```python
a = [5,4,3,6,7,8,9]
```


```python
sum(a)
```




    42




```python
min(a)
```




    3




```python
max(a)
```




    9




```python
a = [5,4,3,6,7,8,9]
```


```python
def f(x):
    return x+1
```


```python
list(map(f,a))
```




    [6, 5, 4, 7, 8, 9, 10]




```python
"Mitsos".find('q')
```




    -1




```python
'Mitsos'.index('q')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-166-5ac49b51bd93> in <module>
    ----> 1 'Mitsos'.index('q')
    

    ValueError: substring not found



```python
[5,4,3,6,7,8,9] + 1
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-153-062de0023e23> in <module>
    ----> 1 [5,4,3,6,7,8,9] + 1
    

    TypeError: can only concatenate list (not "int") to list



```python
def f(a,b):
    return a+b

def g(a,b):
    return a-b

l = [f,g]

op = '+'
op1 = 10
op2 = 5

l['+-'.index(op)](op1, op2)


```




    15




```python
def f():
    print ("mitsos")
    
a = f()
print (a)
```

    mitsos
    None



```python
print (a)
```

    None



```python
def f():
    return "Mitsos"

a = f()
```


```python
print (a)
```

    Mitsos



```python
4
5
6
7
8

```




    8




```python
def f():
    return "mitsos"
f()

def g():
    return "kwstas"
g()
```




    'kwstas'




```python
1
2
3
None
```


```python
print (None)
```

    None



```python
a = [1,2,3,4,5,6]
```


```python
def f(x):
    return x/2

list(map(f,a))
```




    [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]




```python
a
```




    [1, 2, 3, 4, 5, 6]




```python
def f(x):
    return x%2==0
```


```python
list(filter(f, a))
```




    [2, 4, 6]




```python
map(f,a)
```




    <map at 0x7f833ec4e8b0>




```python
def f(x):
    print ("hello")
    return x/2


```


```python
map(f,a)
```




    <map at 0x7f833ec4efa0>




```python
list(map(f,a))
```

    hello
    hello
    hello
    hello
    hello
    hello





    [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]




```python
a = [4,5,3,4,6,7,8,7]
print(a)
```

    [4, 5, 3, 4, 6, 7, 8, 7]



```python
a
```




    [3, 4, 4, 5, 6, 7, 7, 8]




```python
sorted(a)
```




    [3, 4, 4, 5, 6, 7, 7, 8]




```python
a
```




    [4, 5, 3, 4, 6, 7, 8, 7]




```python
a.sort()
```


```python
a
```




    [3, 4, 4, 5, 6, 7, 7, 8]




```python
a = [4,5,3,4,6,7,8,7]
```


```python
b=sorted(a)
```


```python
a
```




    [4, 5, 3, 4, 6, 7, 8, 7]




```python
b
```




    [3, 4, 4, 5, 6, 7, 7, 8]




```python
sorted(a, reverse=False)
```




    [3, 4, 4, 5, 6, 7, 7, 8]




```python
sorted(['patras', 'athens', 'heraklion'])
```




    ['athens', 'heraklion', 'patras']




```python
a
```




    [4, 5, 3, 4, 6, 7, 8, 7]




```python
a.sort()
```


```python
a
```




    [3, 4, 4, 5, 6, 7, 7, 8]




```python
a = [4, 5, 3, 4, 6, 7, 8, 7]
b=sorted(a)

```


```python
a
```




    [4, 5, 3, 4, 6, 7, 8, 7]




```python
a = [4, 5, 3, 4, 6, 7, 8, 7]
sorted(a, reverse=True)
```




    [8, 7, 7, 6, 5, 4, 4, 3]




```python
sorted(['patras', 'athens', 'heraklion'])
```




    ['athens', 'heraklion', 'patras']




```python
'athens' < 'heraklion'
```




    True




```python
'aaaaaaaaaaaaaaaaaaaaa' < 'b'
```




    True




```python
'a' < 'b'
```




    True




```python
'aa' < 'ab'
```




    True




```python
'aa' < 'aab'
```




    True




```python
5<3
```




    False




```python
[3] < [5]
```




    True




```python
[3,5] < [3,6]
```




    True




```python
[3,5,1,1,1,1,1,1] < [3,6]
```




    True




```python
1 < "mitsos"
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-233-14144e7b0975> in <module>
    ----> 1 1 < "mitsos"
    

    TypeError: '<' not supported between instances of 'int' and 'str'



```python
[5, 1] < [6, "mitsos"]
```




    True




```python
[6, 1] < [6, [5, 1] < [6, "mitsos"]]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-235-3962cd0a0ec3> in <module>
    ----> 1 [6, 1] < [6, "mitsos"]
    

    TypeError: '<' not supported between instances of 'int' and 'str'



```python
[3,5,7] <[3,6,5]
```




    True




```python
[3,5] < [3,5,7]
```




    True




```python
[3,5] < [3,5]
```




    False




```python
5<5
```




    False




```python
'athens' < 'heraklion'
```




    True




```python
[4_000_000, 'athens'] < [200_000, 'heraklion']
```




    False




```python
min( [ [4_000_000, 'athens'] , [200_000, 'heraklion'] ] )[1]
```




    'heraklion'




```python
a = [[4_000_000, 'athens'],[200_000, 'heraklion'],[250_000, 'patras']]
```


```python
a = [
    [4_000_000, 'athens'],
    [200_000, 'heraklion'],
    [250_000, 'patras']
]
```


```python
a = [
    [4_000_000, 'athens'],
    [200_000, 'heraklion'],
    [250_000, 'patras'],
]
```


```python
a
```




    [[4000000, 'athens'], [200000, 'heraklion'], [250000, 'patras']]




```python
sorted(a)
```




    [[200000, 'heraklion'], [250000, 'patras'], [4000000, 'athens']]




```python
sorted(a, reverse=True)
```




    [[4000000, 'athens'], [250000, 'patras'], [200000, 'heraklion']]




```python
min(a)
```




    [200000, 'heraklion']




```python
max(a)
```




    [4000000, 'athens']




```python
a = ['athens', 'heraklion', 'lamia']
```


```python
sorted(a)
```




    ['athens', 'heraklion', 'lamia']




```python
def f(x):
    return len(x)
```


```python
sorted(a, key=f)
```




    ['lamia', 'athens', 'heraklion']




```python
sorted(a, key=f, reverse=True)
```




    ['heraklion', 'athens', 'lamia']




```python
a = [[4000000, 'athens'], [250000, 'patras'], [200000, 'heraklion']]
```


```python
sorted(a)
```




    [[200000, 'heraklion'], [250000, 'patras'], [4000000, 'athens']]




```python
a = [['athens',4000000,], [ 'patras', 250000,], [ 'heraklion', 200000,],]
```


```python
a
```




    [['athens', 4000000], ['patras', 250000], ['heraklion', 200000]]




```python
sorted(a)
```




    [['athens', 4000000], ['heraklion', 200000], ['patras', 250000]]




```python
def f(x):
    return x[1]
sorted(a,key=f)
```




    [['heraklion', 200000], ['patras', 250000], ['athens', 4000000]]




```python
min(a, key=f)
```




    ['heraklion', 200000]




```python
a
```




    [['athens', 4000000], ['patras', 250000], ['heraklion', 200000]]




```python
max(a, key=f)
```




    ['athens', 4000000]




```python
max(a, key=f)[0]
```




    'athens'




```python
( sorted(a,key=f)  )  [len(a)//2]
```




    ['patras', 250000]




```python

```


```python
a
```




    [['athens', 4000000], ['patras', 250000], ['heraklion', 200000]]




```python
sorted(a, key=f)
```




    [['heraklion', 200000], ['patras', 250000], ['athens', 4000000]]




```python
b=[4,5,6,7,8,]
```


```python
b[len(b)//2]
```




    6




```python

```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-278-177ba617805e> in <module>
    ----> 1 b[2.5]
    

    TypeError: list indices must be integers or slices, not float



```python

```
