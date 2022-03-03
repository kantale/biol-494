```python
3+6
```




    9




```python
a = 3
```


```python
a
```




    3




```python
a = 3+1
```


```python
b = a + 1
```


```python
b
```




    5




```python
a=2
```


```python
a = a + 1
```


```python
a
```




    3




```python
a
```




    3




```python
a = 'mitsos'
```


```python
a = 1
```


```python
a = a + 1
```


```python
a
```




    2




```python
a += 1
```


```python
a
```




    3




```python
a += 5
```


```python
a = a + 5 # a += 5
```


```python
'the result is: ' + 5 
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-19-167711dab34c> in <module>
    ----> 1 'the result is: ' + 5
    

    TypeError: can only concatenate str (not "int") to str



```python
'the result is: ' + str(5) 
```




    'the result is: 5'




```python
str(5)
```




    '5'




```python
int('5')
```




    5




```python
'the result is: {}'.format(5)
```




    'the result is: 5'




```python
'the result is: a={} b={}'.format(5,4)
```




    'the result is: a=5 b=4'




```python
'the result is: a={value_1} b={value_2}'.format(value_1=5,value_2=4)
```




    'the result is: a=5 b=4'




```python
value_1=5
value_2=8
```


```python
'the result is: a={value_1} b={value_2}'
```




    'the result is: a={value_1} b={value_2}'




```python
f'the result is: a={value_1} b={value_2}'
```




    'the result is: a=5 b=8'



# functions


```python
def f(x):
    return x+1
```


```python
f(5)
```




    6




```python
a = f(5)
```


```python
44
55
66
77
88
99

```




    99




```python
33
```




    33




```python
a=33
```


```python
def f(x):
    return x+1
```


```python
f(4)
```




    5




```python
a=f(4)
```


```python
def f_1(x):
    print(x+1)
    
def f_2(x):
    return(x+1)
```


```python
print (f_1(4))
```

    5
    None



```python
def f_1(x):
    a = 1/x
    return a
```


```python
b = f_1(0)
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-67-35e28f46ee6f> in <module>
    ----> 1 b = f_1(0)
    

    <ipython-input-66-c95a100a34ae> in f_1(x)
          1 def f_1(x):
    ----> 2     a = 1/x
          3     return a


    ZeroDivisionError: division by zero



```python
f_1(4)
```

    5



```python
f_2(4)
```




    5




```python
a = f_1(4)
```

    5



```python
b = f_2(4)
```


```python
b
```




    5




```python
print (a)
```

    None



```python
True
```




    True




```python
False
```




    False




```python
def f(a,b):
    return a+b
```


```python
f(5,3)
```




    8




```python
def f():
    return 'alex'
```


```python
f()
```




    'alex'




```python
def my_precious_thesis():
    read_data()
    do_amazing_analysis()
    
```


```python
def f(x):
    return x+1, x-1
```


```python
a,b = f(4)
```


```python
a
```




    5




```python
b
```




    3




```python
def f(x):
    return x+1
    #print(x+1)

def g(x):
    #return f(x)*10
    print (f(x)*10)

a = g(3)
print(f'a={a}')
```

    40
    a=None



```python

```


```python

```


```python
def f(a,b=4):
    return a+b
```


```python
f(5)
```




    9




```python
f(1,2)
```




    3




```python
None * 10
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-81-fa0e44c8132b> in <module>
    ----> 1 None * 10
    

    TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'



```python
a=2
def f():
    a=3
    
f()
print (a)
```

    2



```python
a=22
def f():
    print (a)
    
f()
```

    22



```python
a=22
def f():
    print (a)
    a=2
    
f()
```


    ---------------------------------------------------------------------------

    UnboundLocalError                         Traceback (most recent call last)

    <ipython-input-90-8c323de482ac> in <module>
          4     a=2
          5 
    ----> 6 f()
    

    <ipython-input-90-8c323de482ac> in f()
          1 a=22
          2 def f():
    ----> 3     print (a)
          4     a=2
          5 


    UnboundLocalError: local variable 'a' referenced before assignment



```python
a=2
def f():
    a=3
    print (a)
f()
print (a)

```

    3
    2



```python
a=2
def f():
    global a # ίουουουουου
    print (a)
f()
print (a)

```

    2
    2



```python
a=3
def f():
    a=4
    def g():
        a=5
        print(a)
        
    g()
    
f()
```

    5



```python
a=3
def f():
    a=4
    def g():
        #a=5
        global a
        print(a)
        
    g()
    
f()
```

    3



```python
a=3
def f():
    a=4
    def g():
        #a=5
        #global a
        nonlocal a
        print(a)
        
    g()
    
f()
```

    4



```python
a=3
def f():
    a=4
    def g():
        a=5
        def e():
            a=6
            def h():
                #a=7
                #global a
                nonlocal a
                print (a)
            h()
        e()
    g()
f()
```

    6



```python
def f(x):
    def g(y):
        return y+1
    return g(2*x)

f(3)
```




    7




```python
a=3
b=a
a=4
print (b)
```

    3



```python
def f(x):
    return x+1

g=f

g(4)
```




    5




```python
def f(x):
    return x+1

g=f

def f(x):
    return x+2

#f(2)
g(2)
```




    3




```python
a=3
def f(x):
    return x+1
```


```python
callable(f)
```




    True




```python
callable(a)
```




    False




```python
callable(g)
```




    True




```python
a=3
```


```python
a(4)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-112-331eaaf84436> in <module>
    ----> 1 a(4)
    

    TypeError: 'int' object is not callable


# if 


```python
a=3
if a > 1:
    print ('ok')

```

    ok



```python
a=0
if a > 1:
    print ('ok')

```


```python
a=0
if a > 1:
    print ('ok')
else:
    print ('hello')

```

    hello



```python
a=0
if a > 1:
    print ('ok')
elif a>2:
    print ('alex')
else:
    print ('hello')
```

    hello



```python
c
```

    ok



```python
a=2.5
if a > 1:
    print ('ok')
elif a>2:
    print ('alex')
else:
    print ('hello')
```

    ok



```python
a=1.5
if a>2:
    print ('alex')
elif a > 1:
    print ('ok')
else:
    print ('hello')
```

    ok



```python
a=1.5
if a>2:
    print ('alex')
elif a > 1:
    print ('ok')
elif a == 1.5:
    print ('sdsds')
else:
    print ('hello')
```

    ok



```python
def f(x):
    return (x+1)
```


```python
if a>1:
    print ('ok')
```


```python
def f():
    return 5
```


```python
a = None

if a:
    print ('ok')
else:
    print ('not ok')
```

    not ok



```python
a = 3

b = a > 3
print (b)
```

    False



```python
def f(x):
    return x+1

if f:
    print ('ok')
```

    ok



```python
bool(f)
```




    True




```python
a = 2
if a = 3:
    print ('ok')
```


      File "<ipython-input-142-4d5f1fe04051>", line 2
        if a = 3:
             ^
    SyntaxError: invalid syntax




```python
def f(n):
    if n%2 == 0:
        return True
    else:
        return False
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
    if n%2 == 0:
        return True
    return False
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
5 % 2 == 0
```




    False




```python
4 % 2 == 0
```




    True




```python
def f(n):
    return n % 2 == 0
```


```python
def disekto(n):
    if n%4 == 0:
        if n%100 == 0:
            if n%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
```


```python
disekto(2000)
```




    True




```python
def bmi(weight, height):
    b = weight / (height**2)
    
    if b<18.5:
        return 'underweight'
    elif b>=18.5 and b<25:
        return 'normal'
    else:
        return 'overweight'
    
```


```python
bmi(18.5 ,1)
```




    'normal'




```python
def bmi(weight, height):
    b = weight / (height**2)
    
    if b<18.5:
        return 'underweight'
    elif b<25:
        return 'normal'
    else:
        return 'overweight'
```


```python
def bmi(weight, height):
    
    def c_bmi():
        return weight / (height**2)
    
    b = c_bmi()
    print (b)
        
    if b<18.5:
        return 'underweight'
    elif b<25:
        return 'normal'
    else:
        return 'overweight'
```


```python
bmi(70, 1.5)
```

    31.11111111111111





    'overweight'




```python

```
