## Αρχεία


```python
!pwd
```

    /Users/admin/Downloads



```python
with open('Homo_sapiens.gene_info', 'r') as f:
    l = f.readline()
    print (l)
```

    #tax_id	GeneID	Symbol	LocusTag	Synonyms	dbXrefs	chromosome	map_location	description	type_of_gene	Symbol_from_nomenclature_authority	Full_name_from_nomenclature_authority	Nomenclature_status	Other_designations	Modification_date	Feature_type
    



```python
with open('Homo_sapiens.gene_info') as f:
    l = f.readlines()
    #print (l)
```


```python
len(l)
```




    61719




```python
l[1000]
```




    '9606\t1218\tCMD1B\t-\tCMPD1|FDC\tMIM:600884\t9\t9q13-q22\tcardiomyopathy, dilated 1B (autosomal dominant)\tunknown\t-\t-\t-\t-\t20191002\t-\n'




```python
with open('Homo_sapiens.gene_info') as f:
    l = f.read()
```


```python
len(l)
```




    13502145




```python
!ls -l Homo_sapiens.gene_info
```

    -rw-r--r--@ 1 admin  staff  13502145 Mar 19 11:54 Homo_sapiens.gene_info



```python
with open('Homo_sapiens.gene_info') as f:
    for line in f:
        print (line)
        break

```

    #tax_id	GeneID	Symbol	LocusTag	Synonyms	dbXrefs	chromosome	map_location	description	type_of_gene	Symbol_from_nomenclature_authority	Full_name_from_nomenclature_authority	Nomenclature_status	Other_designations	Modification_date	Feature_type
    



```python
with open('file.txt', 'w') as f:
    f.write('123\n')
    f.write('456\n')
```


```python
!cat file.txt
```

    123
    456



```python
with open('file.txt', 'x') as f:
    f.write('123\n')
    f.write('456\n')
```


    ---------------------------------------------------------------------------

    FileExistsError                           Traceback (most recent call last)

    <ipython-input-14-c92598bdd549> in <module>
    ----> 1 with open('file.txt', 'x') as f:
          2     f.write('123\n')
          3     f.write('456\n')


    FileExistsError: [Errno 17] File exists: 'file.txt'



```python
with open('file2.txt', 'x') as f:
    f.write('123\n')
    f.write('456\n')
```


```python
with open('file2.txt', 'a') as f:
    f.write('789\n')
    f.write('666\n')
```


```python
!cat file2.txt
```

    123
    456
    789
    666



```python
def f(x):
    with open('file2.txt', 'a') as f:
        f.write(x + '\n')
        
f('Mitsos')
```


```python
!cat file2.txt
```

    123
    456
    789
    666
    Mitsos



```python
%%writefile file.txt


this is a test

```

    Overwriting file.txt



```python
!cat file.txt

```

    
    
    this is a test



```python
with open('file.txt') as f:
    d = f.read()
print (d)
```

    
    
    this is a test
    



```python
%%timeit

l = [1,2,3,4,5,6,7,8,9,10]
def f(x):
    return x%2==1

list(filter(f, l))
```

    1.66 µs ± 94.5 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)



```python
%%timeit

l = [1,2,3,4,5,6,7,8,9,10]

[x for x in l if x%2==1]
```

    887 ns ± 55.6 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)



```python
f1 = open('Homo_sapiens.gene_info')
f2 = open('Homo_sapiens.gene_info')

```


```python
f1.readline()
```




    '9606\t2\tA2M\t-\tA2MD|CPAMD5|FWP007|S863-7\tMIM:103950|HGNC:HGNC:7|Ensembl:ENSG00000175899\t12\t12p13.31\talpha-2-macroglobulin\tprotein-coding\tA2M\talpha-2-macroglobulin\tO\talpha-2-macroglobulin|C3 and PZP-like alpha-2-macroglobulin domain-containing protein 5|alpha-2-M\t20210316\t-\n'




```python
f2.readline()
```




    '#tax_id\tGeneID\tSymbol\tLocusTag\tSynonyms\tdbXrefs\tchromosome\tmap_location\tdescription\ttype_of_gene\tSymbol_from_nomenclature_authority\tFull_name_from_nomenclature_authority\tNomenclature_status\tOther_designations\tModification_date\tFeature_type\n'




```python
f1.close()
```


```python
f2.readline()
```




    '9606\t1\tA1BG\t-\tA1B|ABG|GAB|HYST2477\tMIM:138670|HGNC:HGNC:5|Ensembl:ENSG00000121410\t19\t19q13.43\talpha-1-B glycoprotein\tprotein-coding\tA1BG\talpha-1-B glycoprotein\tO\talpha-1B-glycoprotein|HEL-S-163pA|epididymis secretory sperm binding protein Li 163pA\t20210302\t-\n'




```python
f2.close()
```


```python
f1 = open('file.txt', 'w')
```


```python
f2 = open('file.txt', 'w')
```


```python
!cat file.txt
```


```python
f1.write('111\n')
```




    4




```python
!cat file.txt
```


```python
f1.flush()
```


```python
!cat file.txt
```

    111



```python
f2.write('222\n')
```




    4




```python
!cat file.txt
```

    111



```python
f2.flush()
```


```python
!cat file.txt
```

    222



```python
f1.close()
```


```python
f2.close()
```

### Serialization


```python
a = [1,2,3, {"a": 4, "b": [4,5,6,7]}, [5,6,7,]]
```


```python
with open('file.txt', 'w') as f:
    f.write(str(a))
```


```python
!cat file.txt
```

    [1, 2, 3, {'a': 4, 'b': [4, 5, 6, 7]}, [5, 6, 7]]


```python
b = [1, 2, 3, {'a': 4, 'b': [4, 5, 6, 7]}, [5, 6, 7]]
```


```python
import json
```


```python
b = json.dumps(a)
```


```python
type(b)
```




    str




```python
c = json.loads(b)
```


```python
c == a
```




    True




```python
with open('data.json', 'w') as f:
    json.dump(a, f)
```


```python
!cat data.json

```

    [1, 2, 3, {"a": 4, "b": [4, 5, 6, 7]}, [5, 6, 7]]


```python
with open('data.json', 'r') as f:
    c = json.load(f)
```


```python
c == a
```




    True




```python
json.dumps({1,2,3})
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-72-f6a0a593b80d> in <module>
    ----> 1 json.dumps({1,2,3})
    

    ~/anaconda3/lib/python3.8/json/__init__.py in dumps(obj, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys, **kw)
        229         cls is None and indent is None and separators is None and
        230         default is None and not sort_keys and not kw):
    --> 231         return _default_encoder.encode(obj)
        232     if cls is None:
        233         cls = JSONEncoder


    ~/anaconda3/lib/python3.8/json/encoder.py in encode(self, o)
        197         # exceptions aren't as detailed.  The list call should be roughly
        198         # equivalent to the PySequence_Fast that ''.join() would do.
    --> 199         chunks = self.iterencode(o, _one_shot=True)
        200         if not isinstance(chunks, (list, tuple)):
        201             chunks = list(chunks)


    ~/anaconda3/lib/python3.8/json/encoder.py in iterencode(self, o, _one_shot)
        255                 self.key_separator, self.item_separator, self.sort_keys,
        256                 self.skipkeys, _one_shot)
    --> 257         return _iterencode(o, 0)
        258 
        259 def _make_iterencode(markers, _default, _encoder, _indent, _floatstr,


    ~/anaconda3/lib/python3.8/json/encoder.py in default(self, o)
        177 
        178         """
    --> 179         raise TypeError(f'Object of type {o.__class__.__name__} '
        180                         f'is not JSON serializable')
        181 


    TypeError: Object of type set is not JSON serializable



```python
json.dumps(lambda x : x+1)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-73-e092f9923bfe> in <module>
    ----> 1 json.dumps(lambda x : x+1)
    

    ~/anaconda3/lib/python3.8/json/__init__.py in dumps(obj, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys, **kw)
        229         cls is None and indent is None and separators is None and
        230         default is None and not sort_keys and not kw):
    --> 231         return _default_encoder.encode(obj)
        232     if cls is None:
        233         cls = JSONEncoder


    ~/anaconda3/lib/python3.8/json/encoder.py in encode(self, o)
        197         # exceptions aren't as detailed.  The list call should be roughly
        198         # equivalent to the PySequence_Fast that ''.join() would do.
    --> 199         chunks = self.iterencode(o, _one_shot=True)
        200         if not isinstance(chunks, (list, tuple)):
        201             chunks = list(chunks)


    ~/anaconda3/lib/python3.8/json/encoder.py in iterencode(self, o, _one_shot)
        255                 self.key_separator, self.item_separator, self.sort_keys,
        256                 self.skipkeys, _one_shot)
    --> 257         return _iterencode(o, 0)
        258 
        259 def _make_iterencode(markers, _default, _encoder, _indent, _floatstr,


    ~/anaconda3/lib/python3.8/json/encoder.py in default(self, o)
        177 
        178         """
    --> 179         raise TypeError(f'Object of type {o.__class__.__name__} '
        180                         f'is not JSON serializable')
        181 


    TypeError: Object of type function is not JSON serializable



```python
def f(x):
    return x+1
json.dump(x)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-74-d589213418b1> in <module>
          1 def f(x):
          2     return x+1
    ----> 3 json.dump(x)
    

    NameError: name 'x' is not defined



```python
import pickle
```


```python
a
```




    [1, 2, 3, {'a': 4, 'b': [4, 5, 6, 7]}, [5, 6, 7]]




```python
a.append({3,4,5,6})
```


```python
a.append(f)
```


```python
a = a[:-2]
```


```python
a.append({2,3,4,5})
```


```python
a.append(lambda x : x+1)
```


```python
json.dumps(a)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-81-2f50cf32d976> in <module>
    ----> 1 json.dumps(a)
    

    ~/anaconda3/lib/python3.8/json/__init__.py in dumps(obj, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys, **kw)
        229         cls is None and indent is None and separators is None and
        230         default is None and not sort_keys and not kw):
    --> 231         return _default_encoder.encode(obj)
        232     if cls is None:
        233         cls = JSONEncoder


    ~/anaconda3/lib/python3.8/json/encoder.py in encode(self, o)
        197         # exceptions aren't as detailed.  The list call should be roughly
        198         # equivalent to the PySequence_Fast that ''.join() would do.
    --> 199         chunks = self.iterencode(o, _one_shot=True)
        200         if not isinstance(chunks, (list, tuple)):
        201             chunks = list(chunks)


    ~/anaconda3/lib/python3.8/json/encoder.py in iterencode(self, o, _one_shot)
        255                 self.key_separator, self.item_separator, self.sort_keys,
        256                 self.skipkeys, _one_shot)
    --> 257         return _iterencode(o, 0)
        258 
        259 def _make_iterencode(markers, _default, _encoder, _indent, _floatstr,


    ~/anaconda3/lib/python3.8/json/encoder.py in default(self, o)
        177 
        178         """
    --> 179         raise TypeError(f'Object of type {o.__class__.__name__} '
        180                         f'is not JSON serializable')
        181 


    TypeError: Object of type set is not JSON serializable



```python
pickle.dumps(a)
```


    ---------------------------------------------------------------------------

    PicklingError                             Traceback (most recent call last)

    <ipython-input-91-e346a7b9f67a> in <module>
    ----> 1 pickle.dumps(a)
    

    PicklingError: Can't pickle <function <lambda> at 0x7faf82583ca0>: attribute lookup <lambda> on __main__ failed



```python
with open('file.pickle', 'w') as f2:
    pickle.dump(a, f2)
```


    ---------------------------------------------------------------------------

    PicklingError                             Traceback (most recent call last)

    <ipython-input-90-81309c48e28e> in <module>
          1 with open('file.pickle', 'w') as f2:
    ----> 2     pickle.dump(a, f2)
    

    PicklingError: Can't pickle <function <lambda> at 0x7faf82583ca0>: attribute lookup <lambda> on __main__ failed



```python
pickle.dumps(lambda x : x+1)
```


    ---------------------------------------------------------------------------

    PicklingError                             Traceback (most recent call last)

    <ipython-input-92-7d5e9e36d753> in <module>
    ----> 1 pickle.dumps(lambda x : x+1)
    

    PicklingError: Can't pickle <function <lambda> at 0x7faf82583f70>: attribute lookup <lambda> on __main__ failed



```python
def f(x):
    return 3

pickle.dumps(f)
```




    b'\x80\x04\x95\x12\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x01f\x94\x93\x94.'




```python
with open('test.pickle', 'w') as f2:
    pickle.dump([1,2,3,f], f2)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-95-f21cfafd1eb0> in <module>
          1 with open('test.pickle', 'w') as f2:
    ----> 2     pickle.dump([1,2,3,f], f2)
    

    TypeError: write() argument must be str, not bytes


### itertools


```python
from itertools import combinations
```


```python
genes = ['aa', 'bb', 'cc', 'dd']
for k,l in combinations(genes, 2):
    print (k,l)
```

    aa bb
    aa cc
    aa dd
    bb cc
    bb dd
    cc dd



```python
sum(1 for k in combinations(list(range(10)), 2))
```




    45




```python
sum(1 for k in combinations(list(range(49)), 6))
```




    13983816




```python
i=1
for k in combinations(list(range(1,50)), 6):
    i += 1
    print (k)
    if i > 10:
        break
```

    (1, 2, 3, 4, 5, 6)
    (1, 2, 3, 4, 5, 7)
    (1, 2, 3, 4, 5, 8)
    (1, 2, 3, 4, 5, 9)
    (1, 2, 3, 4, 5, 10)
    (1, 2, 3, 4, 5, 11)
    (1, 2, 3, 4, 5, 12)
    (1, 2, 3, 4, 5, 13)
    (1, 2, 3, 4, 5, 14)
    (1, 2, 3, 4, 5, 15)



```python
a = [10,5,2,]
b = [7,6,5,7]

from itertools import product

for x,y in product(a,b):
    print (x,y)

```

    10 7
    10 6
    10 5
    10 7
    5 7
    5 6
    5 5
    5 7
    2 7
    2 6
    2 5
    2 7



```python
import random

a = [random.randint(-40,40) for x in range(100)]
```


```python
print (a)
```

    [28, -4, 2, -21, 9, 11, -7, 25, 22, 39, -29, -22, 21, -32, -24, 3, 9, -1, -4, 26, 11, -8, 20, -11, 8, 26, 33, -1, -28, 22, -21, 23, -5, 26, -19, -29, 27, 38, 5, -9, 16, -17, 16, -35, 6, 33, 37, 18, 21, -21, -40, -18, -17, -16, 29, -18, -2, -7, -6, 25, 12, -36, 39, -15, 6, 29, -13, 22, -25, -6, 39, 27, -3, -31, -32, -25, -19, -5, -6, 2, -15, 25, 2, -21, 38, -15, -15, -25, -9, 4, -33, -1, 20, -15, 29, -21, -16, 7, -5, 37]



```python
b = []
for start, end in combinations(list(range(0, 101)), 2):
    b.append( (sum(a[start:end]), start, end)        ) 
```


```python
max(b)
```




    (254, 0, 49)




```python
sum(a)
```




    94




```python
from itertools import chain

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
```


```python
for x in powerset(list('mitsos')):
    print (''.join(x))
```

    
    m
    i
    t
    s
    o
    s
    mi
    mt
    ms
    mo
    ms
    it
    is
    io
    is
    ts
    to
    ts
    so
    ss
    os
    mit
    mis
    mio
    mis
    mts
    mto
    mts
    mso
    mss
    mos
    its
    ito
    its
    iso
    iss
    ios
    tso
    tss
    tos
    sos
    mits
    mito
    mits
    miso
    miss
    mios
    mtso
    mtss
    mtos
    msos
    itso
    itss
    itos
    isos
    tsos
    mitso
    mitss
    mitos
    misos
    mtsos
    itsos
    mitsos



```python
import inspect

g = lambda x: x/2

f = lambda x : g(x+1)


inspect.getsource(f)
```




    'f = lambda x : g(x+1)\n'




```python
pickle.dumps(f)
```


    ---------------------------------------------------------------------------

    PicklingError                             Traceback (most recent call last)

    <ipython-input-128-6d61f1b895e9> in <module>
    ----> 1 pickle.dumps(f)
    

    PicklingError: Can't pickle <function <lambda> at 0x7faf82198e50>: attribute lookup <lambda> on __main__ failed



```python
a=[1,2,3,4,5,6,7,8,9,0,]
```


```python
a = [
    "asdASD",
    "asdASDasdgfasef",
    "ASDFASDFASDA",
    "sdfgsdfgsdfg",
]
```


```python
def f(x):
    return x+1
    
def f(x,):
    return (x+1)
```

### Regular Expression


```python
a = 'NG_007400.1:g.8638G>T'
```


```python
def validate(x):
    i = a.find(':')
    if i<0:
        return False
    
    if a.count(':') != 1:
        return False
    
    first, second = a.split(':')
    
    

```


```python
import re
```


```python
'...'
```




    '...'




```python
a= re.fullmatch('\d.[ab]', '3hj')
print (a)
```

    None



```python
a= re.fullmatch('\d.[ab]', '3hb')
print (a)
```

    <re.Match object; span=(0, 3), match='3hb'>



```python
a= re.fullmatch('\d\s[ab]+', '3 bbabababababab')
print (a)
```

    <re.Match object; span=(0, 16), match='3 bbabababababab'>



```python
a= re.fullmatch('\d\s[ab]+', '3 ')
print (a)
```

    None



```python
a= re.fullmatch('\d\s[ab]*', '3 ')
print (a)
```

    <re.Match object; span=(0, 2), match='3 '>



```python
a= re.fullmatch('\d\s[ab]*', '3 abababababbbbb')
print (a)
```

    <re.Match object; span=(0, 16), match='3 abababababbbbb'>



```python
a= re.fullmatch('\d\s[ab]?', '3 ababbb')
print (a)
```

    None



```python
a= re.fullmatch('\d\s[ab]?', '3 a')
print (a)
```

    <re.Match object; span=(0, 3), match='3 a'>



```python
a= re.fullmatch('\d\s[ab]?', '3 ')
print (a)
```

    <re.Match object; span=(0, 2), match='3 '>



```python
a = 'NG_007400.1:g.8638G>T'
```


```python
'+6912233456789'
```




    '+6912233456789'




```python
re.fullmatch('\+?\d+', '+324234234')
```




    <re.Match object; span=(0, 10), match='+324234234'>




```python
re.fullmatch('\+?\d+', '324234234')
```




    <re.Match object; span=(0, 9), match='324234234'>




```python
re.fullmatch('\+?\d+', 'a324234234')
```


```python
a = 'NG_007400.1:g.8638G>T'
```


```python
re.fullmatch('\w\w\w', 'sdd')
```




    <re.Match object; span=(0, 3), match='sdd'>




```python
re.fullmatch('\w\w\w', 's1d')
```




    <re.Match object; span=(0, 3), match='s1d'>




```python
re.fullmatch('\w\w\w', 's_d')
```




    <re.Match object; span=(0, 3), match='s_d'>




```python
a = 'NG_007400.1:g.8638G>T'
```


```python
re.fullmatch('\w+\.\d+:[cgpn]\.\d+[ACGT]>[ACGT]', a)
```




    <re.Match object; span=(0, 21), match='NG_007400.1:g.8638G>T'>




```python
a = re.fullmatch('\w+\.\d+:[cgpn]\.\d+[ACGT]>[ACGT]', 'NG_007400.1:g.8638G>T')
print (a)
```

    <re.Match object; span=(0, 21), match='NG_007400.1:g.8638G>T'>



```python
a = re.fullmatch('\w+\.\d+:[cgpn]\.\d+[ACGT]>[ACGT]', 'NG_007400.1:g.8638G>T')
print (a)
```

    <re.Match object; span=(0, 21), match='NG_007400.1:g.8638G>T'>



```python
a = re.fullmatch('(\w+)\.\d+:[cgpn]\.(\d+)[ACGT]>[ACGT]', 'NG_007400.1:g.8638G>T')
print (a)
```

    <re.Match object; span=(0, 21), match='NG_007400.1:g.8638G>T'>



```python
a.group(1)
```




    'NG_007400'




```python
a.group(2)
```




    '8638'




```python
a = re.search('\d+', 'Mit8sos')
print (a)
```

    <re.Match object; span=(3, 4), match='8'>



```python
a = re.fullmatch('\d+', 'Mit8sos')
print (a)
```

    None



```python
a = re.search('^\d+', 'Mit8sos')
print (a)
```

    None



```python
a = re.search('^\d+', '88888Mitsos')
print (a)
```

    <re.Match object; span=(0, 5), match='88888'>



```python
a = re.search('\d+$', 'Mitsos8767')
print (a)
```

    <re.Match object; span=(6, 10), match='8767'>



```python
bool(a)
```




    True




```python
a = re.search('\d+$', 'Mitsos8767HH')
print (a)
bool(a)
```

    None





    False




```python
a = 'a\nb'
print (a)
```

    a
    b



```python
a = r'a\nb'
print (a)
```

    a\nb



```python
name = 'mitsos'
a = f'my name = {name}'
print (a)
```

    my name = mitsos



```python
a = re.search(r'\d+$', 'Mitsos8767')
```


```python
re.match(r'\d', '8afsdfasdf')
```




    <re.Match object; span=(0, 1), match='8'>




```python
re.search(r'^\d', '8afsdfasdf')
```




    <re.Match object; span=(0, 1), match='8'>




```python
re.search(r'^\d...\w$', '5j5jo')
```




    <re.Match object; span=(0, 5), match='5j5jo'>




```python
re.fullmatch(r'\d...\w', '5j5jo')
```




    <re.Match object; span=(0, 5), match='5j5jo'>




```python

re.fullmatch(r'\d{4}', '1456')

```




    <re.Match object; span=(0, 4), match='1456'>




```python
re.fullmatch(r'\w{2,3} \d{4}', 'QQQ 6789')
```




    <re.Match object; span=(0, 8), match='QQQ 6789'>




```python
re.fullmatch(r'[ΑΒΕΖΗΙΚΜΝΟΡΤΧΥ]{2,3} \d{4}', 'ΑΒΕ 6789')
```




    <re.Match object; span=(0, 8), match='ΑΒΕ 6789'>




```python
re.fullmatch(r'[ΑΒΕΖΗΙΚΜΝΟΡΤΧΥ]{2,3} [0123456789]{4}', 'ΑΒΕ 6789')
```




    <re.Match object; span=(0, 8), match='ΑΒΕ 6789'>




```python
re.fullmatch(r'[ΑΒΕΖΗΙΚΜΝΟΡΤΧΥ]{2,3} [0-9]{4}', 'ΑΒΕ 6789')
```




    <re.Match object; span=(0, 8), match='ΑΒΕ 6789'>




```python
re.fullmatch(r'[^ΓΔΘΛΞΠΣΦΨΩ0-9]{2,3} [0-9]{4}', 'ΑΒΕ 6789')
```




    <re.Match object; span=(0, 8), match='ΑΒΕ 6789'>




```python
re.search(r'(a+)', 'aaaaaaaaaaaaaaa')
```




    <re.Match object; span=(0, 15), match='aaaaaaaaaaaaaaa'>




```python
re.search(r'(a+?)', 'aaaaaaaaaaaaaaa')
```




    <re.Match object; span=(0, 1), match='a'>




```python
re.search(r'(an)+?', 'banana')
```




    <re.Match object; span=(1, 3), match='an'>




```python

```
