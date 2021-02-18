```python
5==5,0
```




    (True, 0)




```python
5,0 == 5
```




    (5, False)




```python
5.0 == 5
```




    True




```python
a  =   5
```


```python
a =  5+1
```


```python
print (a)
```

    6



```python
b = a
```


```python
print (b)
```

    6



```python
b = a+3
```


```python
a=3
b=5
c=a+b
```


```python
c
```




    8




```python
b=10
```


```python
c
```




    8




```python
c=a+b
```


```python
c
```




    13




```python
a
```




    3




```python
a = a + 1
```


```python
a
```




    4




```python
a = a + 10
a
```




    14




```python
a = a * 10
```


```python
a
```




    140




```python
a=5
a = a + 1
print (a)
```

    6



```python
a=5
a += 1   # a = a + 1
print (a)
```

    6



```python
a=5
a *= 10   # a = a * 10
print (a)
```

    50



```python
a=3
b='mitsos '
a*b
```




    'mitsos mitsos mitsos '




```python
'mitsos ' * 3
```




    'mitsos mitsos mitsos '




```python
a=3
a > 5
```




    False




```python
b = a>5
```


```python
print(b)
```

    False



```python
def athroisma(a,b):
    return a+b
```


```python
athroisma(5,6)
```




    11




```python
len("mitsos")
```




    6



```
f(x) = 2x+5
```


```python
def f(x):
    return (2*x) + 5
```


```python
f(10)
```




    25




```python
def f():
    return 5
```


```python
f()
```




    5




```python
'   asdfasdf asdf   '.strip()
```




    'asdfasdf asdf'




```python
def f():
    print ('mitsos')
    
def g():
    return 'mitsos'
```


```python
b = f()
```

    mitsos



```python
a=g()
print(a)
```

    mitsos



```python
print(b)
```

    None



```python
a=3
```


```python
type(a)
```




    int




```python
a=3.3
type(a)
```




    float




```python
a=True
type(a)
```




    bool




```python
a=None
type(a)
```




    NoneType




```python
'' == None
```




    False




```python

```


```python
a = g()
```


```python
print (a)
```

    mitsos



```python
# Μία συνάρτηση που τυπώνει το διπλάσια ενός αριθμού:
def f(x):
    print (2*x)
```


```python
# Μία συνάρτηση που επιστρέφει το διπλάσια ενός αριθμού:
def f(x):
    return 2*x
```


```python
b = f(4)
print(b)
```

    8



```python
b
```




    8




```python
def f(x):
    return x+1

def g(x):
    return f(x)*2

g(2)
```




    6




```python
(2+1)*2
```




    6




```python
def f(x):
    b=x
    c=x/2
    return b+c
```


```python
f(10)
```




    15.0




```python
def f(x):
    def g(y):
        return y+1
    
    return g(x/2)

f(10)
```




    6.0




```python

    
g(5)
```




    6




```python
def f(x):
    
    def g(y):
        return y+1
    
    return g(x/2)
```


```python

```


```python
f(10)
```




    6.0




```python

```


```python
def f(x):
    return x+1

a=2
f(a/2)
```




    2.0




```python
def f(x):
    return x+1

f(2)
```




    3




```python
f(10/2)
```




    6.0




```python
a=10
f(a/2)
```




    6.0




```python
f(1)+f(2)
```




    5




```python
def f(x):
    return (x+1)
```


```python
def f(x):
    a=x
    b=x/2
    return a+b
```


      File "<tokenize>", line 3
        b=x/2
        ^
    IndentationError: unindent does not match any outer indentation level



* ΔΙΑΦΟΡΆ ```print```, ```return```
* βασικα εβαλα 2 πραξεις σε μια συναρτηση και μου εβγαλε μονο το αποτέλεσμα της πρωτης


```python
print("mitsos", 1, True)
```

    mitsos 1 True



```python
print ("mitsos")
print ("kostas")
```

    mitsos
    kostas



```python
print("mitsos")
```

    mitsos



```python
return("mitsos")
```


      File "<ipython-input-93-4de9bd7a78c4>", line 1
        return("mitsos")
        ^
    SyntaxError: 'return' outside function




```python
def f(x):
    return x+1

a=f(3)
print (a)
```

    4



```python
def f(x):
    return x+1
    print ("mitsos")
```


```python
a=f(3)
```


```python
def f(a,b):
    return a+b

```


```python
f(4,5)
```




    9



```
ax^2 + bx + c = 0
```


```python
def f(a,b):
    return a+1, b-2

k,l = f(5,4)
```


```python
k
```




    6




```python
l
```




    2




```python
a=2

if a>3:
    print ("mitsos")
    print ("kostas")
```


```python
a=2
print (a>3)
```

    False



```python
a=2

if a>3:
    print ("mitsos")

print ("kostas")
```

    kostas



```python
# Έλεγχος αν ένας αριθμός είναι στο διάστημα: 50,150
a=120
if a>=50 and a<=150:
    print ('inside')
```

    inside



```python
# Έλεγχος αν ένας αριθμός ΔΕΝ είναι στο διάστημα 50,150
a=30
if not (a>=50 and a<=150):
    print ('outside')

```

    outside



```python
a=100
if a < 50 or a > 150:
    print ('outside')
```


```python

```


```python
a=2

if a>3:
    print ("mitsos")
```


```python
a=3

if a>=3:
    print ("mitsos")
    
if a<=3:
    print ('kwstas')
    
#else:
#    print ("kwstas")
```

    mitsos
    kwstas



```python
a=3

if a>=3:
    print("mitsos")
else:
    print('kostas')
```

    mitsos



```python
a=4
if a%2==0:
    print('zugos')
else:
    print('monos')
```

    zugos



```python
11%2
```




    1




```python
bmi = 20

if bmi<=20:
    print ("lipovaris")
if bmi>=20 and bmi<=30:
    print ('normal')  
if bmi>=30:
    print ('overweight')

```

    lipovaris
    normal



```python
bmi = 20

if bmi<=20:
    print ("lipovaris")
elif bmi>=20 and bmi<=30:
    print ('normal')
elif bmi>=30 and bmi<100:
    print ('overweight')

```


```python
bmi = 20

if bmi<=20:
    print ("lipovaris")
elif bmi>=20 and bmi<=30:
    print ('normal')
else:
    print ('overweight')
```

    lipovaris



```python
def f(n):
    return n%2==0
```


```python
f(5)
```




    False




```python
f(4)
```




    True




```python
def f(n):
    if n%2==0:
        return True
    else:
        return False

```


```python
a = b>3
```


```python
if b>3:
    a=True
else:
    a=False
```
