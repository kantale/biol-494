```python
a = ['chr1', "chr2", "chr3", "chr11"]
```


```python
sorted(a)
```




    ['chr1', 'chr11', 'chr2', 'chr3']




```python
b = 'chr2'
```


```python
int(b[-1])
```




    2




```python
def f(x):
    if x[-2] in '0123456789':
        return int(x[-2:])
    return int(x[-1])
```


```python
b = list(map(f,a))
```


```python
b
```




    [1, 2, 3, 11]




```python
c = list(zip(b,a))
```


```python
[x[1] for x in sorted(c)]
```




    ['chr1', 'chr2', 'chr3', 'chr11']




```python
for i in range(10):
    print (i)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9



```python
for i in ['a', 'b']:
    print (i)
```

    a
    b



```python

a=3
while a>0:
    print ("Hello:", a)
    a = a - 1
    # Όταν φτάνειο στο τέλος της λούπας ξαναπάει στη while !!!!
```

    Hello: 3
    Hello: 2
    Hello: 1



```python
for i in [1,2,3]:

    print (i)
```

    1
    2
    3



```python
for i in range(10):
    print (i)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9



```python
a=0
while a<10:
    print (a)
    a += 1
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9



```python
a=0
while a<10:
    
    if a==5:
        a += 1
        continue
    
    print (a)
    a += 1
```

    0
    1
    2
    3
    4
    6
    7
    8
    9



```python
a=0
while a<10:
    
    if a==5:
        break
    
    print (a)
    a += 1
```

    0
    1
    2
    3
    4



```python
a=0
while a<10:
    
    if a==5:
        break
    
    print (a)
    a += 1
else:
    print ("DEN ekana break")
```

    0
    1
    2
    3
    4



```python
a=0
while a<10:
    
    #if a==5:
    #    break
    
    print (a)
    a += 1
else:
    print ("DEN ekana break")
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    DEN ekana break



```python
a=1
for i in range(5):
    a -= 0.1*a
print (a)
```

    0.5904900000000001



```python
height=1
c=0
while height > 0.5:
    height -= 0.1*height
    c = c + 1
    
print(c)
```

    7



```python
print(height)
```

    0.4782969


1+2+3+4+5+6+....


```python
s = 0
current = 0
while s < 1000:
    current += 1
    s += current
    
s
```




    1035




```python
current
```




    45




```python
sum(range(0, 46))
```




    1035




```python
sum(range(0, 45))
```




    990




```python
def is_prime(x):
    
    state = True
    for n in range(2, x):
        if x%n==0:
            state=False
    return state
        
```


```python
is_prime(23)
```




    True




```python
is_prime(9)
```




    False




```python
def is_prime(x):
    
    
    for n in range(2, x):
        if x%n==0:
            return False
        
    return True
```


```python

```


```python
def is_prime(x):
    
    state = True
    for n in range(2, x):
        if x%n==0:
            state=False
            break
            
    return state
        
```


```python
def is_prime_slow(x):
    
    state = True
    for n in range(2, x):
        if x%n==0:
            state=False
    return state
        
```


```python
is_prime_slow(100_000_000)
```




    False




```python
def is_prime_fast(x):
    
    state = True
    for n in range(2, x):
        if x%n==0:
            state=False
            break
            
    return state
```


```python
is_prime_fast(100_000_000)
```




    False




```python
def is_prime_faster(x):
    
    state = True
    for n in range(2, int(x**0.5)+1):
        if x%n==0:
            state=False
            break
            
    return state
```


```python
# add prime number until the sum is greater than 1000000

s=0
c=1
while s<1_000_000:
    if is_prime_fast(c):
        s += c
    c += 1
    
```


```python
s
```




    1001605




```python
c
```




    3944




```python
def f(x):
    return x/2, x*2

```


```python
a = f(10)
```


```python
print (a)
```

    (5.0, 20)



```python
type(a)
```




    tuple




```python
b = [5,20]
```


```python
print (b)
```

    [5, 20]



```python
b[0]=70
```


```python
print(b)
```

    [70, 20]



```python
a= (5,20)
```


```python
print (a)
```

    (5, 20)



```python
a[0] = 70
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-105-bb7e6a73b7ba> in <module>
    ----> 1 a[0] = 70
    

    TypeError: 'tuple' object does not support item assignment



```python
a
```




    (5, 20)




```python
a[1]
```




    20




```python
c = a[1]
```


```python
c += 10
```


```python
a= [1,2]
```


```python
b,c = a
```


```python
b
```




    1




```python
c
```




    2




```python
b,c = (1,2)
print (b)
print (c)
```

    1
    2



```python
def f(x):
    return x/2, x*2
```


```python
a = f(10)
print(a)
```

    (5.0, 20)



```python
a,b = f(10)
print (a)
print (b)
```

    5.0
    20



```python
5,
```




    (5,)




```python
a= [1,2,3]
tuple(a)
```




    (1, 2, 3)




```python
a = (1,2,3)
list(a)
```




    [1, 2, 3]




```python
a=['mitsos', 'kostas', 'elenh']
b=[4,6,8]

```


```python
for i,name in enumerate(a):
    if name=='elenh':
        print (b[i])
```

    8



```python
for thl, name in zip(b,a):
    if name=='elenh':
        print (thl)
```

    8



```python
b[a.index('elenh')]
```




    8




```python
d = {
    "mitsos": 4,
    "kostas": 6,
    "elenh": 8
}
```


```python
type(d)
```




    dict




```python
d['elenh']
```




    8




```python
len(d)
```




    3




```python
len({})
```




    0




```python
d
```




    {'mitsos': 4, 'kostas': 6, 'elenh': 8}




```python
d['maria'] = 10
```


```python
len(d)
```




    4




```python
d['maria']
```




    10




```python
del d['kostas']
```


```python
d
```




    {'mitsos': 4, 'elenh': 8, 'maria': 10}




```python
d['maria'] = 20
```


```python
d
```




    {'mitsos': 4, 'elenh': 8, 'maria': 20}




```python
d['george'] = {'t': 1}
```


```python
d
```




    {'mitsos': 4, 'elenh': 8, 'maria': 20, 'george': {'t': 1}}




```python
d[1] = 4
```


```python
d
```




    {'mitsos': 4, 'elenh': 8, 'maria': 20, 'george': {'t': 1}, 1: 4}




```python
d[False] = "mitsos"
```


```python
d
```




    {'mitsos': 4,
     'elenh': 8,
     'maria': 20,
     'george': {'t': 1},
     1: 4,
     False: 'mitsos'}




```python
d[5.5] = "kostas"
```


```python
d[ [4,5] ] = 5
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-148-933332b3c719> in <module>
    ----> 1 d[ [4,5] ] = 5
    

    TypeError: unhashable type: 'list'



```python
d[ (4,5) ] = 5
```


```python
hash('mitsos')
```




    6714401743874183407




```python
hash((5,6,7))
```




    -1350146935415579984




```python
hash('mitsos')
```




    6714401743874183407




```python
d = {
    "mitsos": 4,
    "kostas": 6,
    "elenh": 8
}

```


```python
'mitsos' in d
```




    True




```python
'george' in d
```




    False




```python
list(d.keys())
```




    ['mitsos', 'kostas', 'elenh']




```python
list(d.values())
```




    [4, 6, 8]




```python
6 in d.values()
```




    True




```python
3 in d.values()
```




    False




```python
d = {
    "mitsos": 4,
    "kostas": 6,
    "elenh": 8
}
```


```python
a = [4,5,6]

for x in a:
    print (x)
```

    4
    5
    6



```python
d = {
    "mitsos": 4,
    "kostas": 6,
    "elenh": 8
}

for x in d:
    print (x)
```

    mitsos
    kostas
    elenh



```python
for x in d:
    print (x, d[x])
```

    mitsos 4
    kostas 6
    elenh 8



```python
for k,v in d.items():
    print (k,v)
```

    mitsos 4
    kostas 6
    elenh 8



```python
list(d.items())
```




    [('mitsos', 4), ('kostas', 6), ('elenh', 8)]




```python
t = [('mitsos', 4), ('kostas', 6), ('elenh', 8)]
```


```python
dict(t)
```




    {'mitsos': 4, 'kostas': 6, 'elenh': 8}




```python
dict([5,6,7])
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-170-624a4c102ded> in <module>
    ----> 1 dict([5,6,7])
    

    TypeError: cannot convert dictionary update sequence element #0 to a sequence



```python
a=[5,6,7]
```


```python
d={}

for x in a:
    d[x] = 2*x
print (d)
```

    {5: 10, 6: 12, 7: 14}



```python
{x:2*x for x in a } # <--- dictionary Comprehenesion
```




    {5: 10, 6: 12, 7: 14}



### sets


```python
a=[1,2,3,2,3,4,3,5,4,6,7,6,5,6,7,8]
```


```python
set(a)
```




    {1, 2, 3, 4, 5, 6, 7, 8}




```python
a = {1,2,3,4,5}
```


```python
a=set([1,2,3,4,5])
```


```python
a
```




    {1, 2, 3, 4, 5}




```python
a = {1,2,3,4}
b = {3,4,5,6}
```


```python
a.union(b)
```




    {1, 2, 3, 4, 5, 6}




```python
a | b
```




    {1, 2, 3, 4, 5, 6}




```python
a.intersection(b)
```




    {3, 4}




```python
a & b
```




    {3, 4}




```python
a - b
```




    {1, 2}




```python
b - a
```




    {5, 6}




```python
(a - b)  | (b - a)
```




    {1, 2, 5, 6}




```python
a
```




    {1, 2, 3, 4}




```python
b
```




    {3, 4, 5, 6}




```python
a.add(7)
```


```python
a
```




    {1, 2, 3, 4, 7}




```python
a - {7}
```




    {1, 2, 3, 4}




```python
len(a)
```




    5




```python
len(set())
```




    0




```python
a = {1,2}
```


```python
a = set()
```


```python
a
```




    set()




```python
a = {1, 2, 3, 4, 7}
```


```python
for x in a:
    print (x)
```

    1
    2
    3
    4
    7



```python
list(a)
```




    [1, 2, 3, 4, 7]




```python
set('alskdjfhasdlkjfhgaslkdjfghsdlkjfghsldkfghsdlkfjghsldkfjghaldkfgh')
```




    {'a', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 's'}




```python
[x%4 for x in range(10)]
```




    [0, 1, 2, 3, 0, 1, 2, 3, 0, 1]




```python
{x%4 for x in range(10)}
```




    {0, 1, 2, 3}




```python
set([x%4 for x in range(10)])
```




    {0, 1, 2, 3}




```python
a=[1,2,3,2,3,4,3,4,5,4,6,7,8,7,8,9,8,7,6,5,3,2]
```


```python
d = {}
for x in a:
    if not x in d:
        d[x]=0
        
    d[x] += 1

print (d)
```

    {1: 1, 2: 3, 3: 4, 4: 3, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1}



```python
d[100]
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-214-5a6d8be5c86f> in <module>
    ----> 1 d[100]
    

    KeyError: 100



```python
100 in d
```




    False




```python
d.get(100, "mitsos")
```




    'mitsos'




```python
d.get(7, "mitsos")
```




    3




```python
a = {4,5,6,7,7}
```


```python
sorted(a)
```




    [4, 5, 6, 7]




```python
a.sort()
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-221-2ed0d7de6146> in <module>
    ----> 1 a.sort()
    

    AttributeError: 'set' object has no attribute 'sort'



```python
sorted(set("s.,djgfhaslkdjghfaslekgfjW;LKDJGHjrihtarejKRJFGHLSKDRFGJSLKDFJGHLS;DKFGJH"))
```




    [',',
     '.',
     ';',
     'D',
     'F',
     'G',
     'H',
     'J',
     'K',
     'L',
     'R',
     'S',
     'W',
     'a',
     'd',
     'e',
     'f',
     'g',
     'h',
     'i',
     'j',
     'k',
     'l',
     'r',
     's',
     't']




```python
set('mitsos')
```




    {'i', 'm', 'o', 's', 't'}




```python
a=[5,6,4,7,3,8,5,7,]
```


```python
a = [[1,2,3], [6,5,6,7,], [3,2]]
```


```python
a.index([3,2])
```




    2




```python
pop_A = [
	['M1', 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 2, 1, 0, 1, 1, 1, 0, 1],
	['M2', 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 1, 0],
	['M3', 1, 1, 1, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 1, 0, 2, 1],
	['M4', 1, 1, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
	['M5', 0, 0, 2, 2, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 0, 2],
	['M6', 0, 0, 1, 0, 2, 0, 0, 0, 1, 1, 2, 2, 2, 0, 0, 0, 1, 0, 0, 0],
	['M7', 0, 0, 2, 1, 1, 1, 0, 2, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0],
	['M8', 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 0, 0, 2],
	['M9', 0, 0, 1, 0, 0, 1, 2, 1, 0, 0, 1, 1, 1, 1, 0, 2, 1, 0, 2, 1],
	['M10', 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
]
```


```python
max([ (x[1:].count(2),x[0] ) for x in pop_A])[1]
```




    'M6'




```python

m = 0

for x in pop_A:
    c = x[1:].count(2)
    if c >= m:
        m = c
        name = x[0]
print (name)
```

    M6



```python

```
