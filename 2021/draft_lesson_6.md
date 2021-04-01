### Αρχεία


```python
!ls -l mim2gene.txt
```

    -rw-r--r--@ 1 admin  staff  904816 Mar 17 17:12 mim2gene.txt



```python
!pwd
```

    /Users/admin/Downloads



```python
# https://www.omim.org/static/omim/data/mim2gene.txt
with open('mim2gene.txt') as f:
    d = f.read()
```


```python
print(d[:1000])
```

    # Copyright (c) 1966-2021 Johns Hopkins University. Use of this file adheres to the terms specified at https://omim.org/help/agreement.
    # Generated: 2021-03-18
    # This file provides links between the genes in OMIM and other gene identifiers.
    # THIS IS NOT A TABLE OF GENE-PHENOTYPE RELATIONSHIPS.
    # MIM Number	MIM Entry Type (see FAQ 1.3 at https://omim.org/help/faq)	Entrez Gene ID (NCBI)	Approved Gene Symbol (HGNC)	Ensembl Gene ID (Ensembl)
    100050	predominantly phenotypes			
    100070	phenotype	100329167		
    100100	phenotype			
    100200	predominantly phenotypes			
    100300	phenotype			
    100500	moved/removed			
    100600	phenotype			
    100640	gene	216	ALDH1A1	ENSG00000165092
    100650	gene/phenotype	217	ALDH2	ENSG00000111275
    100660	gene	218	ALDH3A1	ENSG00000108602
    100670	gene	219	ALDH1B1	ENSG00000137124
    100675	predominantly phenotypes			
    100678	gene	39	ACAT2	ENSG00000120437
    100680	moved/removed			
    100690	gene	1134	CHRNA1	ENSG00000138435
    100700	predominantly phenotypes			
    100710	gene	1140	CHRNB1	ENSG0000017



```python
len(d)
```




    904816




```python
f = open('mim2gene.txt')
```


```python
d = f.read()
```


```python
f.close()
```


```python
with open('mim2gene.txt') as f:
    for line in f:
        #print (line)
        break
```


```python
with open('mim2gene.txt') as f:
    for line in f:
        print (line.strip())
        #break
```


```python
with open('mim2gene.txt') as f:
    for line_number, line in enumerate(f):
        print (line.strip())
        if line_number > 10:
            break
```

    # Copyright (c) 1966-2021 Johns Hopkins University. Use of this file adheres to the terms specified at https://omim.org/help/agreement.
    # Generated: 2021-03-17
    # This file provides links between the genes in OMIM and other gene identifiers.
    # THIS IS NOT A TABLE OF GENE-PHENOTYPE RELATIONSHIPS.
    # MIM Number	MIM Entry Type (see FAQ 1.3 at https://omim.org/help/faq)	Entrez Gene ID (NCBI)	Approved Gene Symbol (HGNC)	Ensembl Gene ID (Ensembl)
    100050	predominantly phenotypes
    100070	phenotype	100329167
    100100	phenotype
    100200	predominantly phenotypes
    100300	phenotype
    100500	moved/removed
    100600	phenotype



```python
with open('mim2gene.txt') as f:
    first_line = f.readline()
    print (first_line)
```

    # Copyright (c) 1966-2021 Johns Hopkins University. Use of this file adheres to the terms specified at https://omim.org/help/agreement.
    



```python
with open('mim2gene.txt') as f:
    first_line = f.readline()
    print (first_line)
    second_line = f.readline()
    print (second_line)
```

    # Copyright (c) 1966-2021 Johns Hopkins University. Use of this file adheres to the terms specified at https://omim.org/help/agreement.
    
    # Generated: 2021-03-17
    



```python
with open('mim2gene.txt') as f:
    for i in range(10):
        line = f.readline()
        print (line.strip())

```

    # Copyright (c) 1966-2021 Johns Hopkins University. Use of this file adheres to the terms specified at https://omim.org/help/agreement.
    # Generated: 2021-03-17
    # This file provides links between the genes in OMIM and other gene identifiers.
    # THIS IS NOT A TABLE OF GENE-PHENOTYPE RELATIONSHIPS.
    # MIM Number	MIM Entry Type (see FAQ 1.3 at https://omim.org/help/faq)	Entrez Gene ID (NCBI)	Approved Gene Symbol (HGNC)	Ensembl Gene ID (Ensembl)
    100050	predominantly phenotypes
    100070	phenotype	100329167
    100100	phenotype
    100200	predominantly phenotypes
    100300	phenotype



```python
with open('mim2gene.txt') as f:
    lines = f.readlines()
```


```python
len(lines)
```




    27097




```python
print (lines[100])
```

    102800	phenotype			
    



```python
f = open('mim2gene.txt')
l_1 = f.readline()
```


```python
print (l_1)
```

    # Copyright (c) 1966-2021 Johns Hopkins University. Use of this file adheres to the terms specified at https://omim.org/help/agreement.
    



```python
f.readline()
```




    '# Generated: 2021-03-17\n'




```python
f.readline()
```




    '# This file provides links between the genes in OMIM and other gene identifiers.\n'




```python
f.close()
```


```python
f = open('mim2gene.txt')
```


```python
f.readline()
```




    '# Copyright (c) 1966-2021 Johns Hopkins University. Use of this file adheres to the terms specified at https://omim.org/help/agreement.\n'




```python
f = open('mim2gene.txt')
for l in f:
    #print ()
    pass
```


```python
f.readline()
```




    ''




```python
f = open('mim2gene.txt')

while True:
    line = f.readline()
    #if line == ''
    if not line:
        break
f.close()
```


```python
s = 'Mitsos'
k = 'Kwstas'
```


```python
if '':
    print ('1')
else:
    print ('2')
```

    2



```python
with open('my_precious.txt', 'w') as f:
    f.write(s)
    f.write(k)
```


```python
!cat my_precious.txt
```

    MitsosKwstas

Για windows:
```
!type my_precious.txt
```


```python
with open('my_precious.txt', 'w') as f:
    f.write(s + '\n')
    f.write(k + '\n')
```


```python
!cat my_precious.txt
```

    Mitsos
    Kwstas



```python
a = [1,2,3,4,5,6]

with open('my_precious.txt', 'w') as f:
    for i in a:
        f.write(str(i) + '\n')

```


```python
!cat my_precious.txt
```

    1
    2
    3
    4
    5
    6



```python
with open('my_precious.txt', 'w') as f:
    f.write(s + ' ' + k + '\n')
```


```python
!cat my_precious.txt

```

    Mitsos Kwstas



```python
a = ['kwstas', 'mitsos', 'maria', 'sadfzsdfsadc']

with open('my_precious.txt', 'w') as f:
    f.write(' '.join(a) + '\n')
```


```python
!cat my_precious.txt
```

    kwstas mitsos maria sadfzsdfsadc



```python
with open('my_precious.txt', 'a') as f:
    f.write('hello world\n')
```


```python
!cat my_precious.txt
```

    kwstas mitsos maria sadfzsdfsadc
    hello world



```python
with open('my_precious.txt', 'r') as f:
    d = f.read()
print (d)
```

    kwstas mitsos maria sadfzsdfsadc
    hello world
    



```python
a = [1,2,3,4,5,6]
```


```python
with open('double.txt', 'w') as f:
    for i in a:
        f.write(str(i*2) + '\n')


with open('half.txt', 'w') as f:
    for i in a:
        f.write(str(i/2) + '\n')
```


```python
!cat double.txt
```

    2
    4
    6
    8
    10
    12



```python
!cat half.txt
```

    0.5
    1.0
    1.5
    2.0
    2.5
    3.0



```python
with open('double.txt', 'w') as f1, open('half.txt', 'w') as f2:
    for i in a:
        f1.write(str(i*2)+'\n')
        f2.write(str(i/1)+'\n')
```


```python
with open('half2.txt', 'a') as f:
    f.write('asdf')
```


```python
!cat half2.txt
```

    asdf


```python
with open('mim2gene.txt') as f:
    for l in f:
        if l[0] == '#':
            continue
        
        print (l)
        break
```

    100050	predominantly phenotypes			
    



```python
l.strip('\n').split('\t')
```




    ['100050', 'predominantly phenotypes', '', '', '']




```python
l
```




    '100050\tpredominantly phenotypes\t\t\t\n'




```python
l.strip('\n')
```




    '100050\tpredominantly phenotypes\t\t\t'




```python
l.strip('\n').split('\t')
```




    ['100050', 'predominantly phenotypes', '', '', '']




```python
'ababa'.split('a')
```




    ['', 'b', 'b', '']




```python
a = [[1,2,3], [4,5,6], [7,8,9]]
```

### String formatting 


```python
name = 'Mitsos'
age = 40
```


```python
'my name is ' + name + ' and my age is: ' + str(age)
```




    'my name is Mitsos and my age is: 40'




```python
'my name is {} and my age is: {}'.format(name, age)
```




    'my name is Mitsos and my age is: 40'




```python
'my name is {onoma} and my age is: {hlikia}'.format(onoma=name, hlikia=age)
```




    'my name is Mitsos and my age is: 40'




```python
f'my name is {name} and my age is: {age}'
```




    'my name is Mitsos and my age is: 40'




```python
'my name is %s and my age is: %s' % (name, age)
```




    'my name is Mitsos and my age is: 40'




```python
a=234/1345
a
```




    0.17397769516728626




```python
'the result is {} .'.format(a)
```




    'the result is 0.17397769516728626 .'




```python
'the result is {0:.3f} .'.format(a)
```




    'the result is 0.174 .'



### pass


```python
a = 1

if a == 1:
    print ('1')
else:
    #print ('not 1')
    pass
```

    1



```python
for i in [1,2,3,5]:
    pass
```


```python
pass
```


```python
print (1)
pass
print (2)
```

    1
    2



```python
if a==1: # too complicated 
    pass
else:
    ....
    
```


      File "<ipython-input-106-9a1fdd3b174b>", line 4
        ....
            ^
    SyntaxError: invalid syntax



### ternary operator


```python
age = 10
if age >= 18:
    state = 'adult'
else:
    state = 'not adult'
```


```python
state
```




    'not adult'




```python
state = 'adult' if age >= 18 else 'not adult'
```

### is operator


```python
a=10
```


```python
type(a) is int
```




    True




```python
a=10
b=10
a is b
```




    True




```python
a==b
```




    True




```python

```




    True




```python
a=1000
b=1000
a is b
```




    False




```python
a = "mitsos"
b = "mitsos"
a==b
```




    True




```python
a is b
```




    True




```python
a = 1000
b = 1000

a == b
```




    True




```python
a is b
```




    False




```python
a=b
```


```python
a is b
```




    True




```python
b += 1
```


```python
a
```




    1000




```python
b
```




    1001




```python
a = 1000
b = 1000
a=b

a+=1
print(b)

```

    1000



```python
a = [1,2,3]
b = [1,2,3]

a=b

b.append(4)
print (a)
```

    [1, 2, 3, 4]



```python
a = [1,2,3]
b = [1,2,3]

b.append(4)
print (a)
```

    [1, 2, 3]



```python
a = [1,2,3]
b = [1,2,3]

a==b

```




    True




```python
a is b
```




    False




```python
a = [1,2,3]
b = [1,2,3]

a=b

a is b
```




    True




```python
a = 3
def f(x):
    a=4
    
f(10)
print(a)
```

    3



```python

a=[1,2,3]
def f(x):
    a.append(5)

f(10)
print (a)

```

    [1, 2, 3, 5]



```python

def f(a):
    a=4

a=2
f(a)
print (a)
```

    2



```python
def f(a):
    a.append(4)

a=[1,2,3]
f(a)
print (a)
```

    [1, 2, 3, 4]



```python

```


```python
int(4).__add__(6)
```




    10



### lambda functions


```python
a = [1,2,3,4,5,6,7,8,9,10]

def f(x):
    return x%2 == 1

list(filter(f, a))
```




    [1, 3, 5, 7, 9]




```python
def g(x):
    return x*2

list(map(g, a))
```




    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]




```python
def g(x):
    return x*2
```


```python
g(10)
```




    20




```python
g = lambda x : (x*2, x/2)
```


```python
a,b = g(10)
print(a)
print (b)
```

    20
    5.0



```python
add = lambda a,b: a+b
```


```python
add(5,4)
```




    9




```python
def g(x):
    print ("hello")
    return x*2
```


```python
a = [1,2,3,4,5,6,7,8,9,10]
```


```python


list(map(lambda x:x*2, a))
```




    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]




```python
list(filter(lambda x:x%2==1, a))
```




    [1, 3, 5, 7, 9]




```python
a = ['edessa', 'Bethleem', 'Thessaloniki']
```


```python
def f(x):
    return x.count('e')

sorted(a, key=f)
```




    ['Thessaloniki', 'edessa', 'Bethleem']




```python
sorted(a, key= lambda x:x.count('e') )
```




    ['Thessaloniki', 'edessa', 'Bethleem']




```python
min(a, key=lambda x:x.count('e') )
```




    'Thessaloniki'




```python
max(a, key=lambda x:x.count('e') )
```




    'Bethleem'




```python
def f(x):
    
    b = lambda y : y*2
    return b(x)
```


```python
f(10)
```




    20




```python
a = [lambda x:x*2, lambda x:x/2]
```


```python
a[0](10)
```




    20




```python
a[1](10)
```




    5.0




```python
a = {}

```


```python
a[lambda x:x*2] = 4
```


```python
hash(lambda x:x*2)
```




    8781085966026




```python
list(a.keys())
```




    [<function __main__.<lambda>(x)>,
     <function __main__.<lambda>(x)>,
     <function __main__.<lambda>(x)>]




```python
a
```




    {<function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4,
     <function __main__.<lambda>(x)>: 4}




```python
a = [1,2,3,4,5,6,7,8,9,10]
```


```python
[2*x for x in a]
```




    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]




```python
list(map(lambda x:x*2, a))
```




    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]




```python
a=[[1,2], [2,3]]
```


```python
b = [tuple(x) for x in a]
```


```python
print (b)
```

    [(1, 2), (2, 3)]



```python
sorted(b, key=lambda x:x[1], reverse=True)
```




    [(2, 3), (1, 2)]




```python
sorted(a, key=lambda x:x[1], reverse=True)
```




    [[2, 3], [1, 2]]




```python
[sum(x) for x in a]
```




    [3, 5]




```python
[sum(x) for x in b]
```




    [3, 5]




```python

```
