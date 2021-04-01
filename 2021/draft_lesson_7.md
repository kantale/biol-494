```python
def f():
    return 3
    return 4
```


```python
f()
```




    3




```python
def g():
    yield 3
    yield 4
```


```python
gen = g()
```


```python
next(gen)
```




    3




```python
next(gen)
```




    4




```python
next(gen)
```


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-133-6e72e47198db> in <module>
    ----> 1 next(gen)
    

    StopIteration: 



```python
def prime_gen():
    yield 1
    n=2
    while True:
        for d in range(2, n-1):
            if n%d==0:
                break
        else:
            yield n
        n+=1
```


```python
gen = prime_gen()
```


```python
next(gen)
```




    1




```python
next(gen)
```




    1




```python
next(gen)
```




    2




```python
next(gen)
```




    3




```python
next(gen)
```




    5




```python
next(gen)
```




    7




```python
next(gen)
```




    313




```python
gen = prime_gen()
sum(next(gen) for i in range(100))
```




    23071




```python
a = ['a', 'b', 'c']
g = enumerate(a)
```


```python
next(g)
```




    (0, 'a')




```python
next(g)
```




    (1, 'b')




```python
next(g)
```




    (2, 'c')




```python
a=[x for x in range(100_000_000)]
```


```python
a[10000]
```




    10000




```python
del a
```


```python
a=(x for x in range(100_000_000))
```


```python
next(a)
```




    0




```python
next(a)
```




    1




```python
next(a)
```




    2




```python
next(a)
```




    3




```python
c = 0
for x in a:
    print (x)
    c += 1
    if c>5:
        break
```

    4
    5
    6
    7
    8
    9



```python
next(a)
```




    10




```python
c = 0
for x in a:
    print (x)
    c += 1
    if c>5:
        break
```

    11
    12
    13
    14
    15
    16



```python
a=(x for x in range(100_000_000))
```


```python
next(a)
```




    0




```python
print (a)
```

    mitsos



```python
a='mitsos'
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
import random
```


```python
random.randint(10,20)
```




    17




```python
random.choice(["heraklion", "athens", "thessaloniki"])
```




    'thessaloniki'




```python
random.sample([1,2,3,4,5,6,7,8], 2)
```




    [5, 8]




```python
random.random()
```




    0.7247444535768666




```python
import program
```


```python
program.my_fabulous_function(10)
```




    20




```python
program.name
```




    'mitsos'




```python
from program import my_fabulous_function
```


```python
my_fabulous_function(10)
```




    20




```python
from random import randint
```


```python
randint(10, 50)
```




    49




```python
from program import *
```


```python
name
```




    'mitsos'




```python
my_fabulous_function(10)
```




    20




```python
import program
```

    hello world!



```python
from program import print_numbers
```

    hello world!



```python
print_numbers(5)
```

    1
    2
    3
    4
    5


### Exceptions


```python
qwertyu
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-bfe75041371e> in <module>
    ----> 1 qwertyu
    

    NameError: name 'qwertyu' is not defined



```python
1/0
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-4-9e1622b385b6> in <module>
    ----> 1 1/0
    

    ZeroDivisionError: division by zero



```python
a={
    "name": "mitsos"
}
a['age']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-5-264634e8a94b> in <module>
          2     "name": "mitsos"
          3 }
    ----> 4 a['age']
    

    KeyError: 'age'



```python
int('mitsos')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-6-24e8b5b4a1dd> in <module>
    ----> 1 int('mitsos')
    

    ValueError: invalid literal for int() with base 10: 'mitsos'



```python
open('dfasdf')
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-7-5d440f3b39dc> in <module>
    ----> 1 open('dfasdf')
    

    FileNotFoundError: [Errno 2] No such file or directory: 'dfasdf'



```python
try:
    a=1/0
except Exception:
    print ('oops')
```

    oops



```python
a=1/0
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-9-023a503edd86> in <module>
    ----> 1 a=1/0
    

    ZeroDivisionError: division by zero



```python
try:
    open('asdfasdf')
    a=1/0
except Exception:
    print ('oops')
```

    oops



```python
print (a)
```

    0.5



```python
try:
    open('dsfsdf')
    a=1/0
except ZeroDivisionError:
    print ('Daireses me to 0')
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-17-4dba8afe5ddf> in <module>
          1 try:
    ----> 2     open('dsfsdf')
          3     a=1/0
          4 except ZeroDivisionError:
          5     print ('Daireses me to 0')


    FileNotFoundError: [Errno 2] No such file or directory: 'dsfsdf'



```python
def g():
    #a=1/0
    open('sdfsd')

def f():
    g()

try:
    f()
except ZeroDivisionError:
    print ('Daireses me to 0')
except FileNotFoundError:
    print ('DEN YPARXEI TO ARXEIO!!!!!')

```

    DEN YPARXEI TO ARXEIO!!!!!



```python



try:
    #a=1/0
    #open('sdfsd')
    int('mitsos')
except ZeroDivisionError:
    print ('Daireses me to 0')
except FileNotFoundError:
    print ('DEN YPARXEI TO ARXEIO!!!!!')
except Exception:
    print ('Kati allo kako sunebei!')
```

    Kati allo kako sunebei!



```python
try:
    #a=1/0
    #open('sdfsd')
    int('mitsos')
except ZeroDivisionError:
    print ('Daireses me to 0')
except FileNotFoundError:
    print ('DEN YPARXEI TO ARXEIO!!!!!')
except:
    print ('Kati allo kako sunebei!')
```

    Kati allo kako sunebei!



```python
try:
    #a=1/0
    #open('sdfsd')
    int('mitsos')
except ZeroDivisionError:
    print ('Daireses me to 0')
except FileNotFoundError:
    print ('DEN YPARXEI TO ARXEIO!!!!!')
except Exception as e:
    print ('Kati allo kako sunebei: ', str(e))
    
print ('aaa')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-27-4423f089ce6e> in <module>
          2     #a=1/0
          3     #open('sdfsd')
    ----> 4     int('mitsos')
          5 except ZeroDivisionError:
          6     print ('Daireses me to 0')


    ValueError: invalid literal for int() with base 10: 'mitsos'



```python
try:
    #a=1/0
    #open('sdfsd')
    int('mitsos')
except ZeroDivisionError:
    print ('Daireses me to 0')
except FileNotFoundError:
    print ('DEN YPARXEI TO ARXEIO!!!!!')
#except Exception as e:
#    print ('Kati allo kako sunebei: ', str(e))
    
print ('aaa')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-28-4423f089ce6e> in <module>
          2     #a=1/0
          3     #open('sdfsd')
    ----> 4     int('mitsos')
          5 except ZeroDivisionError:
          6     print ('Daireses me to 0')


    ValueError: invalid literal for int() with base 10: 'mitsos'



```python
try:
    #a=1/0
    #open('sdfsd')
    int('mitsos')
except ZeroDivisionError:
    print ('Daireses me to 0')
except FileNotFoundError:
    print ('DEN YPARXEI TO ARXEIO!!!!!')
except Exception as e:
    pass # DON'T DO THIS. SHUT UP Exception
    
print ('aaa')
```

    aaa



```python
try:
    #a=1/0
    #open('sdfsd')
    int('mitsos')
except ZeroDivisionError:
    print ('Daireses me to 0')
except FileNotFoundError:
    print ('DEN YPARXEI TO ARXEIO!!!!!')
except Exception as e:
    print ('Kati allo kako sunebei: ', str(e))
finally:
    print ('FINALLY')
    
print ('aaa')
```

    Kati allo kako sunebei:  invalid literal for int() with base 10: 'mitsos'
    FINALLY
    aaa



```python
try:
    #a=1/0
    a=3
    #open('sdfsd')
    #int('mitsos')
except ZeroDivisionError:
    print ('Daireses me to 0')
except FileNotFoundError:
    print ('DEN YPARXEI TO ARXEIO!!!!!')
except Exception as e:
    print ('Kati allo kako sunebei: ', str(e))
finally:
    # Clean up code 
    print ('FINALLY')
    
print ('aaa')
```

    FINALLY
    aaa



```python
try:
    a=1/0
    #a=3
    #open('sdfsd')
    #int('mitsos')

finally:
    # Clean up code 
    x
    
```

    FINALLY



    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-33-5c5c8601f536> in <module>
          1 try:
    ----> 2     a=1/0
          3     #a=3
          4     #open('sdfsd')
          5     #int('mitsos')


    ZeroDivisionError: division by zero



```python
try:
    a=1/0
    #a=3
    #open('sdfsd')
    #int('mitsos')
except ZeroDivisionError:
    print ('Daireses me to 0')
except FileNotFoundError:
    print ('DEN YPARXEI TO ARXEIO!!!!!')
except Exception as e:
    print ('Kati allo kako sunebei: ', str(e))
else:
    print ('Everything was ok!')
finally:
    # Clean up code 
    print ('FINALLY')
    
print ('aaa')
```

    Daireses me to 0
    FINALLY
    aaa



```python
def f(x):
    
    if not type(x) is int:
        raise Exception('ONLY FLOATS PLEASE!')
    
    return x*2
```


```python
f(3.2)
```


    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    <ipython-input-41-8442a3e670e8> in <module>
    ----> 1 f(3.2)
    

    <ipython-input-40-cb498a4e40ae> in f(x)
          2 
          3     if not type(x) is int:
    ----> 4         raise Exception('ONLY FLOATS PLEASE!')
          5 
          6     return x*2


    Exception: ONLY FLOATS PLEASE!



```python
def f(x):
    
    if not type(x) is int:
        raise NotImplementedError('ONLY FLOATS PLEASE!')
    
    return x*2
```


```python
f(3.2)
```


    ---------------------------------------------------------------------------

    NotImplementedError                       Traceback (most recent call last)

    <ipython-input-45-8442a3e670e8> in <module>
    ----> 1 f(3.2)
    

    <ipython-input-44-832e5e363355> in f(x)
          2 
          3     if not type(x) is int:
    ----> 4         raise NotImplementedError('ONLY FLOATS PLEASE!')
          5 
          6     return x*2


    NotImplementedError: ONLY FLOATS PLEASE!



```python
def g():
    yield 1
    yield 2
    yield 3
    
    
list(g())
```




    [1, 2, 3]




```python
gen = g()

while True:
    try:
        a = next(gen)
    except StopIteration:
        break
    print(a)

```

    1
    2
    3



```python
from collections import Counter
```


```python
Counter('asdlkfjhgasldjfasldjfhlakdsgfhlsdkjfghlsdkjfghlsdkjfhgsldkjfgh')
```




    Counter({'a': 4,
             's': 8,
             'd': 8,
             'l': 8,
             'k': 6,
             'f': 8,
             'j': 7,
             'h': 7,
             'g': 6})




```python
Counter([1,2,2,3,4,5,4,5,6,7,8,7,6,5,4,2])
```




    Counter({1: 1, 2: 3, 3: 1, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1})




```python
a = Counter('Mitsos')
print (a)
```

    Counter({'s': 2, 'M': 1, 'i': 1, 't': 1, 'o': 1})



```python
b = Counter('Kostas')
print (b)
```

    Counter({'s': 2, 'K': 1, 'o': 1, 't': 1, 'a': 1})



```python
a+b
```




    Counter({'M': 1, 'i': 1, 't': 2, 's': 4, 'o': 2, 'K': 1, 'a': 1})




```python
from collections import defaultdict
```


```python
a = defaultdict(int)
b = {}
```


```python
a['mitsos']
```




    0




```python
b['mitsos']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-59-4edd9cb0949e> in <module>
    ----> 1 b['mitsos']
    

    KeyError: 'mitsos'



```python
a['kostas'] += 1
```


```python
a['kostas']
```




    1




```python
a = defaultdict(list)
```


```python
a['kostas']
```




    []




```python
a['mitsos'].append(3)
```


```python
a['mitsos']
```




    [3]




```python
Counter('kostas' + 'Mitsos')
```




    Counter({'k': 1, 'o': 2, 's': 4, 't': 2, 'a': 1, 'M': 1, 'i': 1})




```python
!pwd
```

    /Users/admin/Downloads



```python

```
