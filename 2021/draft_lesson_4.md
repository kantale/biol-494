```python
list(range(10,15))
```




    [10, 11, 12, 13, 14]




```python
list(range(10,20,2))
```




    [10, 12, 14, 16, 18]




```python
list(range(20,10,-2))
```




    [20, 18, 16, 14, 12]




```python
a=[True, True, True]
```


```python
a=[True, True, True]
all(a)
```




    True




```python
a=[True, True, False]
all(a)
```




    False




```python
a=[True, True, '']
all(a)
```




    False




```python
if '':
    print ('hello')
else:
    print ('asdfasd')
```

    asdfasd



```python
a=[True, True, 'sdfsdf']
all(a)
```




    True




```python
a=[True, True, 0]
all(a)
```




    False




```python
a=[True, True, []]
all(a)
```




    False




```python
any([False, False, False, True])
```




    True




```python
any([0, '', []])
```




    False




```python
any([0, '', 1, []])
```




    True




```python
"a+b+c".split('+')
```




    ['a', 'b', 'c']




```python
".dsjf lkdjfh alskj alkjdgh   adlkjg    asdlkjfgh ".split()
```




    ['.dsjf', 'lkdjfh', 'alskj', 'alkjdgh', 'adlkjg', 'asdlkjfgh']




```python
a = """
sd;flkgjsd .fklg ds.fg adf
gs
dfg
sd f
gsd 
fg s
f
"""
a.split('\n')
```




    ['',
     'sd;flkgjsd .fklg ds.fg adf',
     'gs',
     'dfg',
     'sd f',
     'gsd ',
     'fg s',
     'f',
     '']




```python
a = ['a', 'b', 'c']
```


```python
"+".join(a)
```




    'a+b+c'




```python
" mitsos ".join(a)
```




    'a mitsos b mitsos c'




```python
a
```




    ['a', 'b', 'c']




```python
''.join(a)
```




    'abc'




```python
list('abc')
```




    ['a', 'b', 'c']




```python
''.join(list('abc'))
```




    'abc'




```python
list(''.join(['a', 'b', 'c']))
```




    ['a', 'b', 'c']




```python
''.join(['a', 'b', 'c'])
```




    'abc'




```python
list('abc')
```




    ['a', 'b', 'c']




```python
list(''.join(['a', 'b', 'c']))
```




    ['a', 'b', 'c']




```python
a = ['a', 'b', 'c']
b = [1,2,3]
c = [True, 5.5, 'Mitsos']
```


```python
list(zip(a,b))
```




    [('a', 1), ('b', 2), ('c', 3)]




```python
list(zip(a,b,c))
```




    [('a', 1, True), ('b', 2, 5.5), ('c', 3, 'Mitsos')]




```python
list(zip(a,a,b,b,b,c))
```




    [('a', 'a', 1, 1, 1, True),
     ('b', 'b', 2, 2, 2, 5.5),
     ('c', 'c', 3, 3, 3, 'Mitsos')]




```python
c = list(zip(a,b))
```


```python
c
```




    [('a', 1), ('b', 2), ('c', 3)]




```python
def f(x):
    return x[1]

list(map(f, c))
```




    [1, 2, 3]




```python
a
```




    ['a', 'b', 'c']




```python
list(enumerate(a))
```




    [(0, 'a'), (1, 'b'), (2, 'c')]




```python
list(zip(range(len(a)),a))
```




    [(0, 'a'), (1, 'b'), (2, 'c')]




```python
list(range(10))
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
list(range(0,10))
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
list(range(3))
```




    [0, 1, 2]




```python
a = ["a", "b","c"]
```




    ['a', 'b', 'c']




```python
list(zip(range(3),a))
```




    [(0, 'a'), (1, 'b'), (2, 'c')]




```python
list(enumerate(a))
```




    [(0, 'a'), (1, 'b'), (2, 'c')]




```python
a.reverse()
```


```python
a
```




    ['c', 'b', 'a']




```python
a = ['a', 'b', 'c']
```


```python
a[::-1]
```




    ['c', 'b', 'a']




```python
a
```




    ['a', 'b', 'c']




```python
a.sort
```




    <function list.sort(*, key=None, reverse=False)>




```python
def f(x):
    return x.replace('1','').replace('2','').replace('3', '')


f('adsfasdq2dq3kjd2hfqi1yoq2uo2ttyu1eyud')


```




    'adsfasdqdqkjdhfqiyoquottyueyud'




```python
'chr16'[-2:]
```




    '16'




```python
if 'chr1'[-2:][0].isdigit():
    
```




    False




```python
'chr16'.replace('chr', '')
```




    '16'




```python
int('chr7'.replace('chr', ''))
```




    7




```python
for a in [4,5,6,7]:
    print ("mitsos")
```

    mitsos
    mitsos
    mitsos
    mitsos



```python
for a in []:
    print ("mitsos")
```


```python
for a in range(10):
    print ("mitsos")
```

    mitsos
    mitsos
    mitsos
    mitsos
    mitsos
    mitsos
    mitsos
    mitsos
    mitsos
    mitsos



```python
for a in [4,5,6,7]:
    print (a)
```

    4
    5
    6
    7



```python
for i in range(1,11):
    print (i, 'fores to 8 kanei', i*8)
```

    1 fores to 8 kanei 8
    2 fores to 8 kanei 16
    3 fores to 8 kanei 24
    4 fores to 8 kanei 32
    5 fores to 8 kanei 40
    6 fores to 8 kanei 48
    7 fores to 8 kanei 56
    8 fores to 8 kanei 64
    9 fores to 8 kanei 72
    10 fores to 8 kanei 80



```python
print(i)
```

    10



```python
for i in ["a", "b", "c"]:
    print (i)
```

    a
    b
    c



```python
for i in [["a", 1], ["b", 2], ["c", 3]]:
    print (i)
```

    ['a', 1]
    ['b', 2]
    ['c', 3]



```python
for i,j in [["a", 1], ["b", 2], ["c", 3]]:
    print (i, j)
```

    a 1
    b 2
    c 3



```python
a=["a", "b", "c"]
b=[1,2,3]

for i,j in zip(a,b):
    print (i,j)
```

    a 1
    b 2
    c 3



```python
list(zip(a,b))
```




    [('a', 1), ('b', 2), ('c', 3)]




```python
for i,j in [('a', 1), ('b', 2), ('c', 3)]:
    print (i,j)
```

    a 1
    b 2
    c 3



```python
for i in 'Mitsos':
    print (i)
```

    M
    i
    t
    s
    o
    s



```python
# kolpo 1
#METRIMA!!!!!!

```


```python
a = [1,2,3,4,3,2,3,4,4,5,6,7,8,]
```


```python
def f(x):
    return x%2==1

len(list(filter(f,a)))
```




    6




```python
sum(map(f, a))
```




    6




```python
list('asdasdas')
```




    ['a', 's', 'd', 'a', 's', 'd', 'a', 's']




```python

c = 0
for x in a:
    if x%2==1:
        c += 1
        
print (c)
```

    6



```python
a
```




    [1, 2, 3, 4, 3, 2, 3, 4, 4, 5, 6, 7, 8]




```python

```


```python
c = 0
for x in a:
    if f(x):
        #c += 1
        c = c + 1
        
print (c)
```

    6



```python
# KOLPO 2
# Pws tsekaroume an mia lista exei mesa ena sugkekrimeno stoixeio



```


```python
a = ["a", "b", "c", "d"]
```


```python
"b" in a
```




    True




```python
"r" in a
```




    False




```python
found = False
for x in a:
    #if x == 'b':
    if x == 'r':
        found = True
        
print (found)
```

    False



```python
1000000 in range(0,1_000_000_001)
```




    True




```python
found = False
for x in range(0,100000001):
    if x == 1:
        found = True
        break
print(found)
```

    True



```python
for x in ['a', "b", "c", "d"]:
    print (x)
    if x=="b":
        break
```

    a
    b



```python
for x in ['a', "b", "c", "d"]:
    if x!='b':
        print (x)
```

    a
    c
    d



```python
for x in ['a', "b", "c", "d"]:
    if x=='b':
        continue
    print (x)
```

    a
    c
    d



```python
for x in ['a', "b", "c", "d"]:
    print (x)
    if x=="r":
        break
else:
    print ("didn't break")
```

    a
    b
    c
    d
    didn't break



```python

for x in a:
    #if x == 'b':
    if x == 'a':
        break
else:
    print ('did not find it')
        
```


```python
"Α" < "α"
```




    True




```python
"A" < "a"
```




    True




```python
c += 1
print (c)
```

    6



```python
c=5
c = c + 1
print (c)
```

    6



```python
# KOLPO 3
# pws kanoyme thn map

```


```python
a = [1,2,3,4,5]
def f(x):
    return x*10
list(map(f,a))
```




    [10, 20, 30, 40, 50]




```python
a = [1,2,3,4,5]
b = []
def f(x):
    return x*10

for x in a:
    b += [f(x)] # h' b.append(f(x))
 
print (b)
```

    [10, 20, 30, 40, 50]



```python
a=[1,2,3,4,5,6,7,8]
def f(x):
    return x%2==1
    
list(filter(f,a))

```




    [1, 3, 5, 7]




```python
# Filter
a=[1,2,3,4,5,6,7,8]
b = []

def f(x):
    return x%2==1

for x in a:
    if f(x):
        b.append(x)
print (b)
```

    [1, 3, 5, 7]



```python
# Map
a=[1,2,3,4,5,6,7,8]
b = []

def f(x):
    return x*10

for x in a:
    b.append(f(x))
print (b)
```

    [10, 20, 30, 40, 50, 60, 70, 80]



```python
# List comprehensions
```


```python
# Map with list comprehensions
b = [f(x) for x in a]
print (b)
```

    [10, 20, 30, 40, 50, 60, 70, 80]



```python
# Filter with list comprehensions
# Filter
a=[1,2,3,4,5,6,7,8]
b = []

def f(x):
    return x%2==1

for x in a:
    if f(x):
        b.append(x)
print (b)


```

    [1, 3, 5, 7]



```python
[x for x in a if f(x) ]
```




    [1, 3, 5, 7]




```python
def f(x):
    return x*10

def g(x):
    return x%2==1

a = [1,2,3,4,5,6,7,8,9,10]

# pare auta pou einai mona kai pollaplasiase ta epi 10
list(map(f, filter(g, a)))
```




    [10, 30, 50, 70, 90]




```python
[f(x) for x in a if g(x)]
```




    [10, 30, 50, 70, 90]




```python
[f(x) for x in a if g(x)] 
```




    [10, 30, 50, 70, 90, 'mitsos']




```python
[f(x) for x in a if g(x)] 
```




    [10, 30, 50, 70, 90]




```python
for x in range(1,11):
    print (x,'fores to 8 kanei:', x*8)
```

    1 fores to 8 kanei: 8
    2 fores to 8 kanei: 16
    3 fores to 8 kanei: 24
    4 fores to 8 kanei: 32
    5 fores to 8 kanei: 40
    6 fores to 8 kanei: 48
    7 fores to 8 kanei: 56
    8 fores to 8 kanei: 64
    9 fores to 8 kanei: 72
    10 fores to 8 kanei: 80



```python
for i in range(1,11):
    for x in range(1,11):
        #print (i,x)
        print (x,'fores to ',i,' kanei:', i*x)
```

    1 fores to  1  kanei: 1
    2 fores to  1  kanei: 2
    3 fores to  1  kanei: 3
    4 fores to  1  kanei: 4
    5 fores to  1  kanei: 5
    6 fores to  1  kanei: 6
    7 fores to  1  kanei: 7
    8 fores to  1  kanei: 8
    9 fores to  1  kanei: 9
    10 fores to  1  kanei: 10
    1 fores to  2  kanei: 2
    2 fores to  2  kanei: 4
    3 fores to  2  kanei: 6
    4 fores to  2  kanei: 8
    5 fores to  2  kanei: 10
    6 fores to  2  kanei: 12
    7 fores to  2  kanei: 14
    8 fores to  2  kanei: 16
    9 fores to  2  kanei: 18
    10 fores to  2  kanei: 20
    1 fores to  3  kanei: 3
    2 fores to  3  kanei: 6
    3 fores to  3  kanei: 9
    4 fores to  3  kanei: 12
    5 fores to  3  kanei: 15
    6 fores to  3  kanei: 18
    7 fores to  3  kanei: 21
    8 fores to  3  kanei: 24
    9 fores to  3  kanei: 27
    10 fores to  3  kanei: 30
    1 fores to  4  kanei: 4
    2 fores to  4  kanei: 8
    3 fores to  4  kanei: 12
    4 fores to  4  kanei: 16
    5 fores to  4  kanei: 20
    6 fores to  4  kanei: 24
    7 fores to  4  kanei: 28
    8 fores to  4  kanei: 32
    9 fores to  4  kanei: 36
    10 fores to  4  kanei: 40
    1 fores to  5  kanei: 5
    2 fores to  5  kanei: 10
    3 fores to  5  kanei: 15
    4 fores to  5  kanei: 20
    5 fores to  5  kanei: 25
    6 fores to  5  kanei: 30
    7 fores to  5  kanei: 35
    8 fores to  5  kanei: 40
    9 fores to  5  kanei: 45
    10 fores to  5  kanei: 50
    1 fores to  6  kanei: 6
    2 fores to  6  kanei: 12
    3 fores to  6  kanei: 18
    4 fores to  6  kanei: 24
    5 fores to  6  kanei: 30
    6 fores to  6  kanei: 36
    7 fores to  6  kanei: 42
    8 fores to  6  kanei: 48
    9 fores to  6  kanei: 54
    10 fores to  6  kanei: 60
    1 fores to  7  kanei: 7
    2 fores to  7  kanei: 14
    3 fores to  7  kanei: 21
    4 fores to  7  kanei: 28
    5 fores to  7  kanei: 35
    6 fores to  7  kanei: 42
    7 fores to  7  kanei: 49
    8 fores to  7  kanei: 56
    9 fores to  7  kanei: 63
    10 fores to  7  kanei: 70
    1 fores to  8  kanei: 8
    2 fores to  8  kanei: 16
    3 fores to  8  kanei: 24
    4 fores to  8  kanei: 32
    5 fores to  8  kanei: 40
    6 fores to  8  kanei: 48
    7 fores to  8  kanei: 56
    8 fores to  8  kanei: 64
    9 fores to  8  kanei: 72
    10 fores to  8  kanei: 80
    1 fores to  9  kanei: 9
    2 fores to  9  kanei: 18
    3 fores to  9  kanei: 27
    4 fores to  9  kanei: 36
    5 fores to  9  kanei: 45
    6 fores to  9  kanei: 54
    7 fores to  9  kanei: 63
    8 fores to  9  kanei: 72
    9 fores to  9  kanei: 81
    10 fores to  9  kanei: 90
    1 fores to  10  kanei: 10
    2 fores to  10  kanei: 20
    3 fores to  10  kanei: 30
    4 fores to  10  kanei: 40
    5 fores to  10  kanei: 50
    6 fores to  10  kanei: 60
    7 fores to  10  kanei: 70
    8 fores to  10  kanei: 80
    9 fores to  10  kanei: 90
    10 fores to  10  kanei: 100



```python
a = [i*x for i in range(1,11) for x in range(1,11)]
```


```python
a = []
for i in range(1,11):
    for j in range(1,11):
        a.append(i*j)

```


```python
a = 'dsf34lkjh2k3jhreETW65TR34'

b = ''
for x in a:
    if not x in '0123456789':
        b += x
print (b)

```

    dsflkjhkjhreETWTR



```python
a = 'dsf34lkjh2k3jhreETW65TR34'

b = ''
for x in a:
    if x in '0123456789':
        continue
    b += x
print (b)
```

    dsflkjhkjhreETWTR



```python
''.join([x for x in a if not x in '0123456789'])
```




    'dsflkjhkjhreETWTR'




```python
a = [1,2,3,4,5,6,7,8,9,10]
```


```python
c = 0
for x in a:
    if x %2==0:
        c+=1
print (c)
```

    5



```python
len([x for x in a if x%2==1])
```




    5




```python
len(['mitsos' for x in a if x%2==1])
```




    5




```python
[x for x in a if x%2==1]
```




    [1, 3, 5, 7, 9]




```python
[x%2==1 for x in a]
```




    [True, False, True, False, True, False, True, False, True, False]




```python
a
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
sum([x%2==1 for x in a])
```




    5




```python
sum(x%2==1 for x in a)
```




    5




```python
a=["a", "b", "c"]
```


```python
a.index(a[-1])
```




    2




```python
a = [1,2,3,4,5,6,7,8,9,10]
all(x%2==1 for x in a)
```




    False




```python
a = [1,2,3,4,5,6,7,8,9,10]
any(x%2==1 for x in a)
```




    True




```python

```
