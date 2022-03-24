```python

a=1
while a<10:
    a+=1     
    print (a)
    
    
```

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
a = [4,5,6,7]
for x in a:
    print (x+1)
```

    5
    6
    7
    8



```python
i = 0
while i<len(a):
    print (a[i]+1)
    i += 1
```

    5
    6
    7
    8



```python
a=5
if a == 5:
    print ("hello")
```

    hello



```python
while a==5:
    print ("hello")
    break
```

    hello



```python
# 1000
# +7% 

x= 1000
c = 0 
while x<2000:
    c += 1
    x = x + 0.07*x
#print(x)
print (c)

```

    11



```python


x= 1000
c = 0 
while True:
    c += 1
    x = x + 0.07*x
    
    if x > 2000:
        break
#print(x)
print (c)

```

    11



```python
x = 1000
while True:
    x = x + 0.07*x
    if x>2000:
        break
```


```python
a = 0
while a<10:
    a += 1
    if a%2 == 1:
        continue
    print (a)
    
```

    2
    4
    6
    8
    10



```python
a = -1
while a<10:
    a += 1
    if a%2 == 1:
        continue
    print (a)
```

    0
    2
    4
    6
    8
    10



```python
def prime(n):
    i = 2
    while i<n:
        if n%i != 0:
            i += 1
            continue
            #return True
            
        else:
            return False
    return True
        
```


```python
for x in range(20, 41):
    print (x, prime(x))
```

    20 False
    21 False
    22 False
    23 True
    24 False
    25 False
    26 False
    27 False
    28 False
    29 True
    30 False
    31 True
    32 False
    33 False
    34 False
    35 False
    36 False
    37 True
    38 False
    39 False
    40 False



```python
def prime_2(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
```


```python
for x in range(20, 41):
    print (x, prime_2(x))
```

    20 False
    21 False
    22 False
    23 True
    24 False
    25 False
    26 False
    27 False
    28 False
    29 True
    30 False
    31 True
    32 False
    33 False
    34 False
    35 False
    36 False
    37 True
    38 False
    39 False
    40 False



```python
def prime_3(n):
    for i in range(2, n):
        if n%i == 0:
            break
    #print (i)
    return i == n-1
        
```


```python
for x in range(20, 41):
    print (x, prime_3(x))
```

    20 False
    21 False
    22 False
    23 True
    24 False
    25 False
    26 False
    27 False
    28 False
    29 True
    30 False
    31 True
    32 False
    33 False
    34 False
    35 False
    36 False
    37 True
    38 False
    39 False
    40 False



```python
def prime_4(n):
    
    exw_kanei_break = False
    for i in range(2, n):
        if n%i == 0:
            exw_kanei_break = True
            break

            
    return not exw_kanei_break
    
```


```python
for x in range(20, 41):
    print (x, prime_4(x))
```

    20 False
    21 False
    22 False
    23 True
    24 False
    25 False
    26 False
    27 False
    28 False
    29 True
    30 False
    31 True
    32 False
    33 False
    34 False
    35 False
    36 False
    37 True
    38 False
    39 False
    40 False



```python
def prime_5(n):
    
    
    for i in range(2, n):
        if n%i == 0:
            break
    else:
        return True
    
    return False
```


```python
for x in range(20, 41):
    print (x, prime_5(x))
```

    20 False
    21 False
    22 False
    23 True
    24 False
    25 False
    26 False
    27 False
    28 False
    29 True
    30 False
    31 True
    32 False
    33 False
    34 False
    35 False
    36 False
    37 True
    38 False
    39 False
    40 False



```python
def prime_6(n):
    
    def f(x):
        return n%x
    
    l = list(range(2,n))
    #print (l)
    k = list(map(f,l))
    #print (k)
    
    return not (0 in k)
```


```python
for x in range(20, 41):
    print (x, prime_6(x))
```

    20 False
    21 False
    22 False
    23 True
    24 False
    25 False
    26 False
    27 False
    28 False
    29 True
    30 False
    31 True
    32 False
    33 False
    34 False
    35 False
    36 False
    37 True
    38 False
    39 False
    40 False



```python
5 in [6,5,7]
```




    True




```python
a = [4,5,6]
```


```python
b = (4,5,6)
```


```python
a[1] = 100
```


```python
b[1] = 100
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-61-d2a3b3af180f> in <module>
    ----> 1 b[1] = 100
    

    TypeError: 'tuple' object does not support item assignment



```python
def f(x):
    return x-1, x+1
```


```python
f(5)
```




    (4, 6)




```python
type('mitsso')
```




    str




```python
type(33)
```




    int




```python
type([4,5,6])
```




    list




```python
type((5,6,7))
```




    tuple




```python
[5]
```




    [5]




```python
(6)
```




    6




```python
(6,)
```




    (6,)




```python
6,
```




    (6,)




```python
6,7,8,9
```




    (6, 7, 8, 9)




```python
a=list(range(1,100_000_000))
```


```python
99_987_344 in a
```




    True




```python
'mitsos' in a
```




    False



# dictionary


```python
a={
    1 : "BRCA2",
    2 : "P53",
    3 : "APOE",
}
```


```python
2 in a
```




    True




```python
a[2]
```




    'P53'




```python
b={
    "BRCA2" : 1,
    "P53" : 70,
    "APOE": 88,
}
```


```python
b['P53']
```




    70




```python
b.values()
```




    dict_values([1, 70, 88])




```python
b.keys()
```




    dict_keys(['BRCA2', 'P53', 'APOE'])




```python
b
```




    {'BRCA2': 1, 'P53': 70, 'APOE': 88}




```python
b['mitsos'] = [4,5,6]
```


```python
b['mitsos'] = {"5": "ASDSWD"}
```


```python
def f(x):
    return x+1
```


```python
b['my_fabulous_f'] = f
```


```python
b['my_fabulous_f'](60)
```




    61




```python
b
```




    {'BRCA2': 1,
     'P53': 70,
     'APOE': 88,
     'mitsos': {'5': 'ASDSWD'},
     'my_fabulous_f': <function __main__.f(x)>}




```python
b[4] = "mitsos"
```


```python
b['mitsos'] = 'mitsos'
```


```python
b[True] = 'mitsos'
```


```python
b[6.66] = 'mitsos'
```


```python
b[ [5,6] ] = 'mitsos'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-101-8fd87e8553e5> in <module>
    ----> 1 b[ [5,6] ] = 'mitsos'
    

    TypeError: unhashable type: 'list'



```python
hash('mitsos123')
```




    -5477650241974683608




```python
hash('mitsos123')
```




    -5477650241974683608




```python
b['P53']
```




    70




```python
b['P53'] += 1
```


```python
b['P53']
```




    71




```python
b
```




    {'BRCA2': 1,
     'P53': 71,
     'APOE': 88,
     'mitsos': 'mitsos',
     'my_fabulous_f': <function __main__.f(x)>,
     4: 'mitsos',
     True: 'mitsos',
     6.66: 'mitsos'}




```python
del b['P53']
```


```python
b
```




    {'BRCA2': 1,
     'APOE': 88,
     'mitsos': 'mitsos',
     'my_fabulous_f': <function __main__.f(x)>,
     4: 'mitsos',
     True: 'mitsos',
     6.66: 'mitsos'}




```python
b['P53'] = 50
```


```python
b['P53'] + 50
```




    100




```python
b['QQQ'] = b['P53']
```


```python
b
```




    {'BRCA2': 1,
     'APOE': 88,
     'mitsos': 'mitsos',
     'my_fabulous_f': <function __main__.f(x)>,
     4: 'mitsos',
     True: 'mitsos',
     6.66: 'mitsos',
     'P53': 50,
     'QQQ': 50}




```python
'P53' in b
```




    True




```python
'XYZ' in b
```




    False




```python
1 in b.values()
```




    True




```python
2 in b.values()
```




    False




```python
c = {'a': 1, 'b':3, 'c': 2,}

for a,b in c.items():
    print (a,b)
```

    a 1
    b 3
    c 2



```python
d = {}
for a,b in c.items():
    d[b]=a
print (d)
```

    {1: 'a', 3: 'b', 2: 'c'}



```python
d = {  b:a  for a,b in c.items()  }
print (d)
```

    {1: 'a', 3: 'b', 2: 'c'}



```python
len(d)
```




    3




```python
len({})
```




    0




```python
c= ['heraklion', 'patras', 'athens']
```


```python
{k:len(k) for k in  c }
```




    {'heraklion': 9, 'patras': 6, 'athens': 6}




```python
d = {'a': 1, 'b':3, 'c': 2,}
```


```python
list(d.items())
```




    [('a', 1), ('b', 3), ('c', 2)]




```python
for a,b in [('a', 1), ('b', 3), ('c', 2)]:  # d.items():
    print (a,b)
```

    a 1
    b 3
    c 2



```python
a = [5,6,7]
b = ['a', 'b', 'c']
```


```python
list(zip(a,b))
```




    [(5, 'a'), (6, 'b'), (7, 'c')]




```python
dict(zip(a,b))
```




    {5: 'a', 6: 'b', 7: 'c'}




```python

```


```python
dict( [ (1,2), (5,6) ]   )
```




    {1: 2, 5: 6}




```python
a = set()
```


```python
len(a)
```




    0




```python
a.add(5)
```


```python
len(a)
```




    1




```python
a.add(6)
```


```python
len(a)
```




    2




```python
a.add(5)
```


```python
len(a)
```




    2




```python
a = set()
```


```python
a = {1,2,3,4,5}
```


```python
3 in a
```




    True




```python
8 in a
```




    False




```python
a = {1,2,3,4,5}
```


```python
b = {4,5,6,7,8}
```


```python
a & b
```




    {4, 5}




```python
a | b
```




    {1, 2, 3, 4, 5, 6, 7, 8}




```python
a - b
```




    {1, 2, 3}




```python
b - a
```




    {6, 7, 8}




```python
a = set()
for x in range(1,100_000_000):
    a.add(x)
```


```python
99_432_433 in a
```




    True




```python
'mitsos' in a
```




    False




```python
100_000_001 in a
```




    False




```python

```


```python
set(range(6,100))
```




    {6,
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
     99}




```python
set([ 3,4,5,4,5,6,7,6,7,8,9,8,7 ])
```




    {3, 4, 5, 6, 7, 8, 9}




```python
set('fghdjsiudfygfhrjekfgiuyfhdjskirug7hufreijhrghtjrkdfuyghgufiehg')
```




    {'7', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'r', 's', 't', 'u', 'y'}




```python
[x%5 for x in range(15)]
```




    [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]




```python
{x:x%5 for x in range(15)}
```




    {0: 0,
     1: 1,
     2: 2,
     3: 3,
     4: 4,
     5: 0,
     6: 1,
     7: 2,
     8: 3,
     9: 4,
     10: 0,
     11: 1,
     12: 2,
     13: 3,
     14: 4}




```python
{x%5 for x in range(15)}
```




    {0, 1, 2, 3, 4}




```python
a = {
    5: [7,8,9],
}
```


```python
{x: list(range(x)) for x in range(10)}
```




    {0: [],
     1: [0],
     2: [0, 1],
     3: [0, 1, 2],
     4: [0, 1, 2, 3],
     5: [0, 1, 2, 3, 4],
     6: [0, 1, 2, 3, 4, 5],
     7: [0, 1, 2, 3, 4, 5, 6],
     8: [0, 1, 2, 3, 4, 5, 6, 7],
     9: [0, 1, 2, 3, 4, 5, 6, 7, 8]}




```python
!pwd
```

    /Users/admin/GENOMED4ALL/AI_MDS_data



```python

```


```python

```
