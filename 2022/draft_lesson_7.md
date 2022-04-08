```python
a = 4
b = a
a += 1
print (b)
```

    4



```python
a = [1,2,3]
b = a
a.append(4)
print (b)
```

    [1, 2, 3, 4]



```python
a = [1,2,3]
b = [1,2,3]
c = a
```


```python
# a.append(4)
a == b
```




    True




```python
a == c
```




    True




```python
a is b 
```




    False




```python
a is c
```




    True




```python
a = [1,2,3]
b = list(a)
```


```python
a is b
```




    False




```python
b = [x for x in a]
```


```python
import copy
```


```python
b = copy.copy(a)
```


```python
def f(x):
    x += 1
```


```python
a = 3
f(a)
print (a)
```

    3



```python
a = [1,2]
def f(x):
    x.append(3)
f(a)
print (a)
```

    [1, 2, 3]



```python
a = [1,2,3]
b = [x+1 for x in a]
print (b)
```

    [2, 3, 4]



```python
def f(x):
    return x+1
a = [1,2,3]
b = list(map(f, a))
print (b)
```

    [2, 3, 4]



```python
a = 3+4
```


```python
3+4 = a
```


      Input In [22]
        3+4 = a
        ^
    SyntaxError: cannot assign to operator




```python
a = 3
if a < 4:
    b = 6
else:
    b = 10
print (b)
```

    6



```python
b = 6 if a<4 else 10
print (b)
```

    6



```python
b = (6 if a<4 else 10) + 10
print (b)
```

    16



```python
b = 3 + 4
```


```python
True and False
```




    False




```python
not False
```




    True




```python
-8
```




    -8




```python
+77
```




    77




```python
bmi = 40
if bmi < 20:
    diag = 'leptos'
elif bmi < 30:
    diag = 'normal'
else:
    diag = 'fat'
```


```python
bmi = 40
if bmi < 20:
    diag = 'leptos'
else:
    if bmi < 30:
        diag = 'normal'
    else:
        diag = 'fat'
```


```python
bmi = 40
if bmi < 20:
    diag = 'leptos'
else:
    diag = 'normal' if bmi < 30 else 'fat'

```


```python
diag = 'leptos' if bmi < 20 else ('normal' if bmi < 30 else 'fat')
```


```python
a = [1,2,3]
b = []
for x in a:
    b.append(x+1)
print (b)
```

    [2, 3, 4]



```python
a = [1,2,3]
b = [x+1 for x in a]
print (b)
```

    [2, 3, 4]



```python
def f(x):
    return x+1
a = [1,2,3]
b= list(map(f, a))
print (b)
```

    [2, 3, 4]



```python
def f(x):
    return x+1
```


```python
f = lambda x : x+1
```


```python
def f(a,b):
    return a+b


```


```python
f = lambda a,b : a+b
```


```python
f(6,7)
```




    13




```python
a = [1,2,3]
b = list(map(lambda x : x+1, a))
print (b)
```

    [2, 3, 4]



```python
a = ['sdfgsdfg', 'sdfgsdfgsadfg', 'shrtytyt4653gg']
```


```python
def f(x):
    return x.count('s')
b = sorted(a, key=f)
print (b)
```

    ['shrtytyt4653gg', 'sdfgsdfg', 'sdfgsdfgsadfg']



```python

b = sorted(a, key=lambda x : x.count('s'))
print (b)
```

    ['shrtytyt4653gg', 'sdfgsdfg', 'sdfgsdfgsadfg']



```python

f = lambda x : x+1

```




    5




```python
(lambda x : x+2)(3)
```




    5




```python
f = lambda x : x+1
```


```python
callable(f)
```




    True




```python
type(f)
```




    function




```python
def f(a):
    def g(b):
        return a+b
    return g
```


```python
aa = f(3)
```


```python
aa(6)
```




    9




```python
f(3)(6)
```




    9




```python
def f(a):
    def g(b):
        return a+b
    return g
```


```python
def f(a):
    return lambda b:a+b
```


```python
f = lambda a: lambda b:a+b
```


```python
f(3)(6)
```




    9



# Generators


```python
def f(x):
    return x+1

b = map(f, [1,2,3])
#print (list(b))
```


```python

```


```python
b
```




    <map at 0x1cf94c19700>




```python
next(b)
```




    2




```python
next(b)
```




    3




```python
next(b)
```




    4




```python
next(b)
```


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    Input In [71], in <cell line: 1>()
    ----> 1 next(b)


    StopIteration: 



```python
def f():
    return 3
    return 4
    return 5
```


```python
a = f()
print (a)
```

    3



```python
def f():
    yield 3
    yield 4
    yield 5
    yield 6
```


```python
a  = f()
print (a)
```

    <generator object f at 0x000001CF96762350>



```python
next(a)
```




    3




```python
next(a)
```




    4




```python
next(a)
```




    5




```python
a = f()
```


```python
type(a)
```




    generator




```python
def f():
    yield 3
    yield 4
    yield 5
    yield 6
```


```python
a = f()
```


```python
next(a)
```




    3




```python
next(a)
```




    4




```python
list(a)
```




    [5, 6]




```python
def f():
    yield 3
    yield 4
    yield 5
    yield 6
```


```python
for x in f():
    print (x)
```

    3
    4
    5
    6



```python
def f():
    yield 3
    yield 4
    yield 5
    yield 6
```


```python
a = f()
next(a)
next(a)
for x in a:
    print (x)
```

    5
    6



```python
type(f)
```




    function




```python
g = f()
```


```python
type(g)
```




    generator




```python
a = [2,3,4]
b = [x+1 for x in a]
print (b)
```

    [3, 4, 5]



```python
def f():
    for x in a:
        yield x+1
```


```python
g = f()
```


```python
next(g)
```




    3




```python
next(g)
```




    4




```python
next(g)
```




    5




```python
a = [2,3,4]
b = (x+1 for x in a)
```


```python
type(b)
```




    generator




```python
next(b)
```




    3




```python
a = range(1, 100_000_000_000)
```


```python
b = map(lambda x: x+3, a)
```


```python
c = filter(lambda x:x%2==1, b)
```


```python
d = (int(str(x)[-1]) for x in c)
```


```python
next(d)
```




    5




```python
next(d)
```




    7




```python
next(d)
```




    9




```python
next(d)
```




    1




```python
!dir
```

     Volume in drive C has no label.
     Volume Serial Number is 2E18-E674
    
     Directory of C:\Users\user
    
    06/04/2022  05:25 ££    <DIR>          .
    06/04/2022  05:25 ££    <DIR>          ..
    06/04/2022  03:49 ££    <DIR>          .ipynb_checkpoints
    30/03/2022  03:41 ££    <DIR>          .ipython
    06/04/2022  03:49 ££    <DIR>          .jupyter
    24/02/2022  10:57 §£    <DIR>          3D Objects
    30/03/2022  05:00 ££            12.313 alex.docx
    30/03/2022  05:29 ££               391 alex2.txt
    24/02/2022  10:57 §£    <DIR>          Contacts
    06/04/2022  01:03 ££    <DIR>          Desktop
    30/03/2022  05:00 ££    <DIR>          Documents
    30/03/2022  03:45 ££    <DIR>          Downloads
    24/02/2022  10:57 §£    <DIR>          Favorites
    30/03/2022  05:37 ££                54 findings.txt
    24/02/2022  10:57 §£    <DIR>          Links
    30/03/2022  03:38 ££    <DIR>          miniconda3
    30/03/2022  03:43 ££                19 mitsos.txt
    24/02/2022  10:57 §£    <DIR>          Music
    24/02/2022  12:53 ££    <DIR>          OneDrive
    24/02/2022  10:58 §£    <DIR>          Pictures
    30/03/2022  04:58 ££               488 results.txt
    24/02/2022  10:57 §£    <DIR>          Saved Games
    24/02/2022  10:58 §£    <DIR>          Searches
    06/04/2022  02:51 ££    <DIR>          teaching_VIOT_I
    30/03/2022  06:16 ££            40.623 test_1.ipynb
    06/04/2022  05:25 ££            29.852 Untitled.ipynb
    04/03/2022  01:49 ££    <DIR>          Videos
                   7 File(s)         83.740 bytes
                  20 Dir(s)  198.915.809.280 bytes free



```python
!type results.txt
```

    this is a fantastic file
    very precious data
    much science. bravo!
    nobel
    
    
    dyjfjfghjfkhjthjhkhkhjfgfgmgdd.fgjdalkgjshdlfkgjhsdlkfjghsldkfjghsldkjghskldfjghlsdkfjhglskdfjghlskdfjghskldjfghsldkfjghsldkjgh sljgsldkj ghskldjgh sldkgjh skldfjgh skldfjghsldkjghsldkfjgh skldjg hsldfkjghsldkjg hsldfkjgh sldkjgh sldkgjh sldkjg hsdlfkjgh sdfkjg hsldkfjg hsldkfjg hsldkfjg hsldkfjg hsldkfjgh sldkfjg sldkfjgh sldkjgh sldfjgh sldkfjgh sldkfjgh sldkfjg hsldkfjg hsldkfjgh sldkfjgh sldkfjgh fjkldh
    
    aaa



```python
f = open('results.txt')
```


```python
next(f)
```




    'this is a fantastic file\n'




```python

```


```python
next(c)
```




    5




```python
next(c)
```




    7




```python
# list(c)
```


```python
%%writefile a.txt
123
234
546
567
687
```

    Overwriting a.txt



```python
def f():
    with open('a.txt') as f:
        for l in f:
            if int(l)%2==1:
                yield l.strip()
```


```python
g = f()
for x in range(2):
    b = next(g)
    print (b)
```

    123
    567



```python

```


```python
g = f()
```


```python
next(g)
```




    '123'




```python
next(g)
```




    '567'




```python
next(g)
```




    '687'




```python
for x in g:
    print (x)
```


```python
import antigravity
```


```python
import this
```

    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!



```python

```


```python
from my_fabulous_code import f # 1
```


```python
f()
```

    hello



```python
from my_fabulous_code import * # IOUOUOU # 3
```


```python
a
```




    'biolohgy'




```python
f()
```

    hello



```python
import my_fabulous_code # 2 
```


```python
my_fabulous_code.a
```




    'biolohgy'




```python
my_fabulous_code.f()
```

    hello



```python
import this
```

    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!



```python
from kostas.mitsos.test import g
```


```python
g()
```

    sdfgsdfg



```python
from collections import Counter
```


```python
Counter('sdklfjghsdlkjghsldkjghsldkjghsldkfjghsldkjghsldkghsldkfjghskldathqruioelg')
```




    Counter({'s': 9,
             'd': 9,
             'k': 9,
             'l': 10,
             'f': 3,
             'j': 7,
             'g': 9,
             'h': 9,
             'a': 1,
             't': 1,
             'q': 1,
             'r': 1,
             'u': 1,
             'i': 1,
             'o': 1,
             'e': 1})




```python
Counter([1,2,3,2,3,4,3,4,6,4,7,8,9])
```




    Counter({1: 1, 2: 2, 3: 3, 4: 3, 6: 1, 7: 1, 8: 1, 9: 1})




```python
a = Counter('faklrutsleaiuhsldkfjghsldkfjghsdkfjghsldjkheailughsakldjhsldkfjgh')
```


```python
b = Counter('sd;kfgjhlaskeryawliefhLAJFGHD;lawrieyueailfj:OAfghsealghsoeaighu')
```


```python
a
```




    Counter({'f': 5,
             'a': 4,
             'k': 7,
             'l': 8,
             'r': 1,
             'u': 3,
             't': 1,
             's': 7,
             'e': 2,
             'i': 2,
             'h': 8,
             'd': 6,
             'j': 6,
             'g': 5})




```python
b
```




    Counter({'s': 4,
             'd': 1,
             ';': 2,
             'k': 2,
             'f': 4,
             'g': 4,
             'j': 2,
             'h': 5,
             'l': 5,
             'a': 6,
             'e': 6,
             'r': 2,
             'y': 2,
             'w': 2,
             'i': 4,
             'L': 1,
             'A': 2,
             'J': 1,
             'F': 1,
             'G': 1,
             'H': 1,
             'D': 1,
             'u': 2,
             ':': 1,
             'O': 1,
             'o': 1})




```python
a + b
```




    Counter({'f': 9,
             'a': 10,
             'k': 9,
             'l': 13,
             'r': 3,
             'u': 5,
             't': 1,
             's': 11,
             'e': 8,
             'i': 6,
             'h': 13,
             'd': 7,
             'j': 8,
             'g': 9,
             ';': 2,
             'y': 2,
             'w': 2,
             'L': 1,
             'A': 2,
             'J': 1,
             'F': 1,
             'G': 1,
             'H': 1,
             'D': 1,
             ':': 1,
             'O': 1,
             'o': 1})




```python
from collections import defaultdict
```


```python
a = {}
```


```python
print (a['mitsos'])
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Input In [13], in <cell line: 1>()
    ----> 1 print (a['mitsos'])


    KeyError: 'mitsos'



```python
a = defaultdict(int)
```


```python
print (a['mitsos'])
```

    0



```python
a = 'aljrgajkfajkldfgskdaghasdljghsdaklfghkldafhsdkljghsklghskldfghskldfjghsldkgh'
```


```python
b = {}
for x in a:
    if not x in b:
        b[x] = 0
    b[x] += 1
    
```


```python
b = defaultdict(int)
for x in a:

    #b[x] += 1
    b[x] = b[x] + 1

```


```python
b = defaultdict(list)

for x in [(1, 'a'), (2,'b'), (1, 'c')]:
    
    b[x[0]].append(x[1])
    
print (b)
    

```

    defaultdict(<class 'list'>, {1: ['a', 'c'], 2: ['b']})



```python
b = {}

for x in [(1, 'a'), (2,'b'), (1, 'c')]:
    
    if not x[0] in b:
        b[x[0]] = []
        
    b[x[0]].append(x[1])
    
print (b)
```

    {1: ['a', 'c'], 2: ['b']}



```python
b
```




    defaultdict(int,
                {'a': 7,
                 'l': 10,
                 'j': 6,
                 'r': 1,
                 'g': 10,
                 'k': 10,
                 'f': 6,
                 'd': 9,
                 's': 8,
                 'h': 9})




```python
import random
```


```python
random.random()
```




    0.3170388002120018




```python
random.randint(18,20)
```




    20




```python
counter = 0
N = 1_000_000
for y in range(N): 
    if [random.randint(1, 6) for x in range(10)].count(6) == 3:
        counter += 1
print (counter/N)
```

    0.155197



```python

```


```python

```


```python

```


```python

```


```python

```
