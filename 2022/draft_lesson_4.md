```python
l = ['athens', 'heraklion', 'patras']
min(l)
```




    'athens'




```python
def f(x):
    return x[1]
```


```python
min(l, key=f)
```




    'patras'




```python
l = [
    ['gene_1', 20],
    ['gene_2', 50],
    ['gene_3', 40],
]
```


```python
l[0]
#f(l[0])
```




    ['gene_1', 20]




```python
f(['gene_1', 20])
```




    20




```python
f('mitsos')
```




    'i'




```python
min(l, key=f)
```




    ['gene_1', 20]




```python
max(l, key=f)
```




    ['gene_2', 50]




```python
max(l, key=f)[0]
```




    'gene_2'




```python
[1,2,3,4][0]
```




    1




```python
l = [
    ['gene_1', 20],
    ['gene_2', 50],
    ['gene_3', 40],
]
max(l, key=f)
```




    ['gene_2', 50]




```python
max(l, key=f) # --> ['gene_2', 50]
```




    ['gene_2', 50]




```python
['gene_2', 50][0]
```




    'gene_2'




```python
max(l, key=f)[0]
```




    'gene_2'



Φτιάξτε μία συνάρτηση η οποοία θα παίρνει μία παράμετρ η οποία θα είναι μία λίστα από strings. Η συνάρτηση θα πρέπει να επιστρέφει το στοιχείο της λίστα το οποίο έχει το μικρότερα αλφαβητικά 2ο γράμμα.


```python
def f(x):
    return x[1]

def g(l):
    return min(l, key=f)
```


```python
g(['alex', 'kostas', 'maria'])
```




    'maria'



Φτιάξτε μία συνάρτηση η οποοία θα παίρνει μία παράμετρ η οποία θα είναι μία λίστα από strings. Η συνάρτηση θα πρέπει να επιστρέφει μία νέα λίστα η οποία θα περιέχει το πλήθος από χαρακτήρες που έχουν τα στοιχεία της λίστας της παραμέτρου.


```python
fff(['alex', 'kostas', 'maria']) # [4, 5, 5]
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-19-fc3247754b83> in <module>
    ----> 1 fff(['alex', 'kostas', 'maria']) # [4, 5, 5]
    

    NameError: name 'fff' is not defined



```python
def f2(x):
    return len(x)

def f1(l):
    return list(map(f2, l))
```


```python
f1(['alex', 'kostas', 'maria'])
```




    [4, 6, 5]




```python
l1 = list(range(1,101))
```


```python
all([True, True, True])
```




    True




```python
all([True, True, True, 0])
```




    False




```python
all(['aaa', 'bbb', 'ccc'])
```




    True




```python
all(['aaa', 'bbb', '', 'ccc'])
```




    False




```python
any([False, False, False])
```




    False




```python
any([False, False, 'mitsos', False])
```




    True




```python
any([False, False, True, False])
```




    True




```python
any([])
```




    False




```python
all([])
```




    True




```python
cities= ['athens', 'heraklion', 'patras']
```


```python
population = [4_000_000, 200_000, 180_000]
```


```python
list(zip(cities, population))
```




    [('athens', 4000000), ('heraklion', 200000), ('patras', 180000)]




```python
all_together = list(zip(cities, population))
```


```python
all_together
```




    [('athens', 4000000), ('heraklion', 200000), ('patras', 180000)]




```python
def f(x):
    return x[1]
```


```python
min(all_together, key=f)[0]
```




    'patras'




```python
min(zip(cities, population), key=f)[0]
```




    'patras'




```python
zip(cities, population)
```




    <zip at 0x7fe95c4544c0>




```python
filter(f, cities)
```




    <filter at 0x7fe95c44c4c0>




```python
map(f, cities)
```




    <map at 0x7fe95c44c310>




```python
b = zip(cities, population)
```


```python
b
```




    <zip at 0x7fe95c4588c0>




```python
list(b)
```




    [('athens', 4000000), ('heraklion', 200000), ('patras', 180000)]




```python
b
```




    <zip at 0x7fe95c4588c0>




```python
b = range(1,1_000_000_001)
```


```python
b = range(1,100_000_000)
```


```python
b
```




    range(1, 100000000)




```python
c = list(b)
```


```python
del c
```


```python
cities
```




    ['athens', 'heraklion', 'patras']




```python
a = [1,2,3,5]
b = [6,7,8]
c = ['a', 'v', 'c']

list(zip(a,b,c))
```




    [(1, 6, 'a'), (2, 7, 'v'), (3, 8, 'c')]




```python
list(zip(a[::3], b))
```




    [(1, 6), (5, 7)]




```python
a = [5,6,7,6,5,4,5,6,7,2,8,9,7,6]
```


```python
min(a)
```




    2




```python
a.index(min(a))
```




    9




```python
list(enumerate(a))
```




    [(0, 5),
     (1, 6),
     (2, 7),
     (3, 6),
     (4, 5),
     (5, 4),
     (6, 5),
     (7, 6),
     (8, 7),
     (9, 2),
     (10, 8),
     (11, 9),
     (12, 7),
     (13, 6)]




```python
def f(x):
    return x[1]
```


```python
min(enumerate(a), key=f)
```




    (9, 2)




```python
min(enumerate(a), key=f)[0]
```




    9




```python
l = [6,7,8,9]

for x in l:
    print ('mitsos')
    print (x)
    print ('kostas')
```

    mitsos
    6
    kostas
    mitsos
    7
    kostas
    mitsos
    8
    kostas
    mitsos
    9
    kostas



```python
for x in l:
    
    if x in [6,8]:
        continue
    
    print ('mitsos')
    print (x)
    print ('kostas')
```

    mitsos
    7
    kostas
    mitsos
    9
    kostas



```python
for x in l:
    
    #print ('mitsos')
    print (x)
    #print ('kostas')
    
    if x in [6,8]:
        continue
```

    6
    7
    8
    9



```python
l = [1,2,3,4,5,6,7,8,9,10]
for x in l:
    
    #if x <= 5:
    #    print (x)
```

    1
    2
    3
    4
    5



```python
for x in l:
    a=x
    print (a)
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10



```python
for x in l:
    a=x
    if x <= 5:
        print (a)
```

    1
    2
    3
    4
    5



```python
for x in l:
    a=x
    print (a)
    if x <= 5:
        print (a)
```

    1
    1
    2
    2
    3
    3
    4
    4
    5
    5
    6
    7
    8
    9
    10



```python
a = list(range(1,101))
def f1(x):
    return [a,x]

b = list(map(f1, a))

def f2(k):
    
    def f3(x):
        return x%k==0
    
    return f3

    
```


```python
list(map(f2(b[0][1]), b[0][0]))
```




    [True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True]




```python
a
```




    [1,
     2,
     3,
     4,
     5,
     6,
     7,
     8,
     9,
     10,
     11,
     12,
     13,
     14,
     15,
     16,
     17,
     18,
     19,
     20,
     21,
     22,
     23,
     24,
     25,
     26,
     27,
     28,
     29,
     30,
     31,
     32,
     33,
     34,
     35,
     36,
     37,
     38,
     39,
     40,
     41,
     42,
     43,
     44,
     45,
     46,
     47,
     48,
     49,
     50,
     51,
     52,
     53,
     54,
     55,
     56,
     57,
     58,
     59,
     60,
     61,
     62,
     63,
     64,
     65,
     66,
     67,
     68,
     69,
     70,
     71,
     72,
     73,
     74,
     75,
     76,
     77,
     78,
     79,
     80,
     81,
     82,
     83,
     84,
     85,
     86,
     87,
     88,
     89,
     90,
     91,
     92,
     93,
     94,
     95,
     96,
     97,
     98,
     99,
     100]




```python
l = [1,2,3,4,5,6,7,8,9,10]
for x in l:
    print (x)
    if x <= 5:
        print (x+10)
```

    1
    11
    2
    12
    3
    13
    4
    14
    5
    15
    6
    7
    8
    9
    10



```python
l = [1,2,3,4,5,6,7,8,9,10]
for x in l:
    print (x)
    if x > 5:
        continue
    print (x+10)
```

    1
    11
    2
    12
    3
    13
    4
    14
    5
    15
    6
    7
    8
    9
    10



```python
l = [12,5,18,8,7,20]

for x in l:
    if x <10:
        continue
        
    print (x)

```

    12
    18
    20



```python

l = [1,2,3,4,5,6,7,8,9,10]
for x in l:
    print (x)
    
    if x > 5:
        break
    
```

    1
    2
    3
    4
    5
    6



```python
for x in l:
    if x > 5:
        break
    print (x)
```

    1
    2
    3
    4
    5



```python
for x in 'mitsos':
    print (x)
```

    m
    i
    t
    s
    o
    s



```python
for x in [[1,2], [6,7], [7,8]]:
    print (x)
```

    [1, 2]
    [6, 7]
    [7, 8]



```python
a=3
```


```python
a,b = [4,5]
```


```python
a
```




    4




```python
b
```




    5




```python
for x,y in [[1,2], [6,7], [7,8]]:
    print (f'{x}+{y}={x+y}')
```

    1+2=3
    6+7=13
    7+8=15



```python
l = [2,3,4,5,6,7,8,]
```


```python
def f(x):
    return x+10

list(map(f, l))
```




    [12, 13, 14, 15, 16, 17, 18]




```python
k = []
for x in l:
    k.append(x+10)
print (k)
```

    [12, 13, 14, 15, 16, 17, 18]



```python
k = []
for x in l:
    k += [x+10]
print (k)
```

    [12, 13, 14, 15, 16, 17, 18]



```python
k = [x+10 for x in l]
print (k)
```

    [12, 13, 14, 15, 16, 17, 18]



```python
l = [5,6,7,8,9,10,11]
```


```python
def f(x):
    return sum(x)
```


```python
f(l)
```




    56




```python
def f2(x):
    return x+10
f(map(f2, l))
```




    126




```python
k = []
for x in l:
    k += [x+10]
f(k)
```




    126




```python
f( [x+10 for x in l] )
```




    126




```python
[x+10 for x in l] + ['mitsos']
```




    [15, 16, 17, 18, 19, 20, 21, 'mitsos']




```python
l = [2,3,4,5,6,7,8,9,10]
```


```python
k = []
for x in l:
    if x>5:
        k.append(x+10)
        
k
```




    [16, 17, 18, 19, 20]




```python
[ x+10 for x in l if x>5  ]
```




    [16, 17, 18, 19, 20]




```python
l
```




    [2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
for x in range(1,11):
    print (f'{x} times 5 is {x*5}')
```

    1 times 5 is 5
    2 times 5 is 10
    3 times 5 is 15
    4 times 5 is 20
    5 times 5 is 25
    6 times 5 is 30
    7 times 5 is 35
    8 times 5 is 40
    9 times 5 is 45
    10 times 5 is 50



```python
for y in range(1,11):
    for x in range(1,11):
        #print (y,x)
        print (f'{x} times {y} is {x*y}')
```

    1 times 1 is 1
    2 times 1 is 2
    3 times 1 is 3
    4 times 1 is 4
    5 times 1 is 5
    6 times 1 is 6
    7 times 1 is 7
    8 times 1 is 8
    9 times 1 is 9
    10 times 1 is 10
    1 times 2 is 2
    2 times 2 is 4
    3 times 2 is 6
    4 times 2 is 8
    5 times 2 is 10
    6 times 2 is 12
    7 times 2 is 14
    8 times 2 is 16
    9 times 2 is 18
    10 times 2 is 20
    1 times 3 is 3
    2 times 3 is 6
    3 times 3 is 9
    4 times 3 is 12
    5 times 3 is 15
    6 times 3 is 18
    7 times 3 is 21
    8 times 3 is 24
    9 times 3 is 27
    10 times 3 is 30
    1 times 4 is 4
    2 times 4 is 8
    3 times 4 is 12
    4 times 4 is 16
    5 times 4 is 20
    6 times 4 is 24
    7 times 4 is 28
    8 times 4 is 32
    9 times 4 is 36
    10 times 4 is 40
    1 times 5 is 5
    2 times 5 is 10
    3 times 5 is 15
    4 times 5 is 20
    5 times 5 is 25
    6 times 5 is 30
    7 times 5 is 35
    8 times 5 is 40
    9 times 5 is 45
    10 times 5 is 50
    1 times 6 is 6
    2 times 6 is 12
    3 times 6 is 18
    4 times 6 is 24
    5 times 6 is 30
    6 times 6 is 36
    7 times 6 is 42
    8 times 6 is 48
    9 times 6 is 54
    10 times 6 is 60
    1 times 7 is 7
    2 times 7 is 14
    3 times 7 is 21
    4 times 7 is 28
    5 times 7 is 35
    6 times 7 is 42
    7 times 7 is 49
    8 times 7 is 56
    9 times 7 is 63
    10 times 7 is 70
    1 times 8 is 8
    2 times 8 is 16
    3 times 8 is 24
    4 times 8 is 32
    5 times 8 is 40
    6 times 8 is 48
    7 times 8 is 56
    8 times 8 is 64
    9 times 8 is 72
    10 times 8 is 80
    1 times 9 is 9
    2 times 9 is 18
    3 times 9 is 27
    4 times 9 is 36
    5 times 9 is 45
    6 times 9 is 54
    7 times 9 is 63
    8 times 9 is 72
    9 times 9 is 81
    10 times 9 is 90
    1 times 10 is 10
    2 times 10 is 20
    3 times 10 is 30
    4 times 10 is 40
    5 times 10 is 50
    6 times 10 is 60
    7 times 10 is 70
    8 times 10 is 80
    9 times 10 is 90
    10 times 10 is 100



```python
a=3
b=543
f'the result is {a**b}'
```




    'the result is 11935519118492731861170453326995581060398381482285334349106220115773223294149524291209185193062334151951263338145978000005419852343067049171344263624658770848526822548919097505597663169917391029784291289028924390538821554118075054639153642342604979742268547627'




```python
#[ for y in range(1,11) for x in range(1,11) ]
```


```python
[[x,y] for y in ['a', 'b', 'c'] for x in [5,7] ]
```




    [[5, 'a'], [7, 'a'], [5, 'b'], [7, 'b'], [5, 'c'], [7, 'c']]




```python
k = [f'{x}X{y}={x*y}' for y in range(1,11) for x in range(1,11)]


```


```python
#print ('\n'.join(k))
print ('\n'.join([f'{x}X{y}={x*y}' for y in range(1,11) for x in range(1,11)]))
```

    1X1=1
    2X1=2
    3X1=3
    4X1=4
    5X1=5
    6X1=6
    7X1=7
    8X1=8
    9X1=9
    10X1=10
    1X2=2
    2X2=4
    3X2=6
    4X2=8
    5X2=10
    6X2=12
    7X2=14
    8X2=16
    9X2=18
    10X2=20
    1X3=3
    2X3=6
    3X3=9
    4X3=12
    5X3=15
    6X3=18
    7X3=21
    8X3=24
    9X3=27
    10X3=30
    1X4=4
    2X4=8
    3X4=12
    4X4=16
    5X4=20
    6X4=24
    7X4=28
    8X4=32
    9X4=36
    10X4=40
    1X5=5
    2X5=10
    3X5=15
    4X5=20
    5X5=25
    6X5=30
    7X5=35
    8X5=40
    9X5=45
    10X5=50
    1X6=6
    2X6=12
    3X6=18
    4X6=24
    5X6=30
    6X6=36
    7X6=42
    8X6=48
    9X6=54
    10X6=60
    1X7=7
    2X7=14
    3X7=21
    4X7=28
    5X7=35
    6X7=42
    7X7=49
    8X7=56
    9X7=63
    10X7=70
    1X8=8
    2X8=16
    3X8=24
    4X8=32
    5X8=40
    6X8=48
    7X8=56
    8X8=64
    9X8=72
    10X8=80
    1X9=9
    2X9=18
    3X9=27
    4X9=36
    5X9=45
    6X9=54
    7X9=63
    8X9=72
    9X9=81
    10X9=90
    1X10=10
    2X10=20
    3X10=30
    4X10=40
    5X10=50
    6X10=60
    7X10=70
    8X10=80
    9X10=90
    10X10=100



```python

metritis = 0
for x in range(1,46):
    for y in range(x+1,46):
        for z in range(y+1,46):
            for a in range(z+1,46):
                for b in range(a+1,46):
                    for t in range(1,21):
                        #print (x,y,z,a,b,t)
                        metritis += 1
                        if metritis % 1000000 == 0:
                            print (metritis)
print (metritis)

```

    1000000
    2000000
    3000000
    4000000
    5000000
    6000000
    7000000
    8000000
    9000000
    10000000
    11000000
    12000000
    13000000
    14000000
    15000000
    16000000
    17000000
    18000000
    19000000
    20000000
    21000000
    22000000
    23000000
    24000000
    24435180



```python
len([
'a'

for x in range(1,46)
    for y in range(x+1,46)
        for z in range(y+1,46)
            for a in range(z+1,46)
                for b in range(a+1,46)
                    for t in range(1,21)
                      if x+y==z
])
```




    1421420




```python
a=5
a += 1
a
```




    6




```python
a = 5
a = a+ 1 # a += 1
a

```




    6




```python

metritis = 0

metritis += 1
metritis += 1
metritis += 1
metritis += 1
metritis += 1
metritis += 1


print (metritis)
```

    6



```python
for x in range(1,6):
    for y in range(10,15):
        print (x,y)
```

    1 10
    1 11
    1 12
    1 13
    1 14
    2 10
    2 11
    2 12
    2 13
    2 14
    3 10
    3 11
    3 12
    3 13
    3 14
    4 10
    4 11
    4 12
    4 13
    4 14
    5 10
    5 11
    5 12
    5 13
    5 14



```python
list(range(10,15))
```




    [10, 11, 12, 13, 14]




```python

```
