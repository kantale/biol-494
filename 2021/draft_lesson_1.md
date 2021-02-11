

```python
3243523452345234523452348956293847569238475692387465293874569238745629834765923874569283746529387456
```




    3243523452345234523452348956293847569238475692387465293874569238745629834765923874569283746529387456




```python
3+2
```




    5




```python
3-2
```




    1




```python
3*2
```




    6




```python
3/2
```




    1.5




```python
3//2
```




    1




```python
10//3
```




    3




```python
4**2
```




    16




```python
5%2
```




    1




```python
5.0
```




    5.0




```python
5
```




    5




```python
"mitsos"
```




    'mitsos'




```python
"5"
```




    '5'




```python
5
```




    5




```python
"mitsos" + "kostas"
```




    'mitsoskostas'




```python
"mitsos" + " " + "kostas"
```




    'mitsos kostas'




```python
""
```




    ''




```python
" "
```




    ' '




```python
"mitsos" * 5
```




    'mitsosmitsosmitsosmitsosmitsos'




```python
"*" * 50
```




    '**************************************************'




```python
"Asdfasdf" - 5
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-24-a8acfcb129a3> in <module>()
    ----> 1 "Asdfasdf" - 5
    

    TypeError: unsupported operand type(s) for -: 'str' and 'int'



```python
"dfasdfasdf".count('a')
```




    2




```python
"aaa bbb ccc".replace("bbb", "ppp")
```




    'aaa ppp ccc'




```python
"aaa bbb ccc".replace("b", "ppp")
```




    'aaa ppppppppp ccc'




```python
"asdfasdfasdfasdf".upper()
```




    'ASDFASDFASDFASDF'




```python
"ASDFASDFASDF".lower()
```




    'asdfasdfasdf'




```python
"αλέξανδρος".upper()
```




    'ΑΛΈΞΑΝΔΡΟΣ'




```python
"abcdefghijklm"[0]
```




    'a'




```python
"abcdefghijklm"[1]
```




    'b'




```python
"abcdefghijklm"[-1]
```




    'm'




```python
"abcdefghijklm"[-2]
```




    'l'




```python
"abcdefghijklm"[2]
```


```python
"abcd"[-2]
```




    'c'




```python
"abcd"[2]
```




    'c'




```python
"abcdefghijklm"[0:3]
```




    'abc'




```python
"abcdefghijklm"[2:6]
```




    'cdef'




```python
"abcdefghijklm"[2:8]
```




    'cdefgh'




```python
""
```




    ''




```python
"a"
```




    'a'




```python
"aaa"[1:2]
```




    'a'




```python
"alexandros"
```




    'alexandros'




```python
'alexandros'
```




    'alexandros'




```python
'asdfasdfa"adfasdfs'
```




    'asdfasdfa"adfasdfs'




```python
"asdfasdfa'adfasdfs"
```




    "asdfasdfa'adfasdfs"




```python
'''dflkgdslk"gj'ha sdfas fdasdf's"ldkfg'''
```




    'dflkgdslk"gj\'ha sdfas fdasdf\'s"ldkfg'




```python
"""dflkgdslk"gj'ha sdfas fdasdf's"ldkfg"""
```




    'dflkgdslk"gj\'ha sdfas fdasdf\'s"ldkfg'




```python
"""
sdfg s.drmgnsd fklgn sd;kfg sdf
gsd f
hs 
fghd f
ghdfdfg sdfg sdfg sdfg sdfg sdfg sfdg 
gh

"""
```




    '\nsdfg s.drmgnsd fklgn sd;kfg sdf\ngsd f\nhs \nfghd f\nghdfdfg sdfg sdfg sdfg sdfg sdfg sfdg \ngh\n\n'




```python
"alksdjhflaskd\nhflaksjfh"
```




    'alksdjhflaskd\nhflaksjfh'




```python
print ("alksdjhflaskd\nhflaksjfh")
```

    alksdjhflaskd
    hflaksjfh



```python
'abcdef\'ghijkml'
```




    "abcdef'ghijkml"




```python
"abcdef'ghijkml"
```




    "abcdef'ghijkml"




```python
"abcdefghijklmn"[3:5]
```




    'de'




```python
"abcdefghijklmn"[100]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-58-a8ba1681a8d5> in <module>()
    ----> 1 "abcdefghijklmn"[100]
    

    IndexError: string index out of range



```python
"abcdefghijklmn"[3:100]
```




    'defghijklmn'




```python
"abcdefghijklmn"[2:10]
```




    'cdefghij'




```python
"abcdefghijklmn"[2:10:2]
```




    'cegi'



```
a b c d e f g h i j k 
0 1 2 3 4 5 6 7 8 9 10
    ^ ^ ^ ^ ^ ^ ^ ^
    2               10
    *   *   *   *
    
```


```python
"abcdefghijklmnopqrst"[2:12:3]
```




    'cfil'




```python
"abcdefghijklmnopqrst"[12:2:-3]
```




    'mjgd'




```python
"abcdefghijklmnopqrst"[1000:2:-3]
```




    'tqnkhe'




```python
"abcdefghijklmnopqrst"[1000:-20000:-3]
```




    'tqnkheb'




```python
"abcdefghijklmnopqrst"[2:5]
```




    'cde'




```python
"abcdefghijklmnopqrst"[0:5]
```




    'abcde'




```python
"abcdefghijklmnopqrst"[:5]
```




    'abcde'




```python
"abcdefghijklmnopqrst"[3:559238452345]
```




    'defghijklmnopqrst'




```python
"abcdefghijklmnopqrst"[3:]
```




    'defghijklmnopqrst'




```python
"abcdefghijklmnopqrst"[3:10:0]
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-83-3b09ce22195e> in <module>()
    ----> 1 "abcdefghijklmnopqrst"[3:10:0]
    

    ValueError: slice step cannot be zero



```python
"abcdefghijklmnopqrst"[3:10:]
```




    'defghij'




```python
"abcdefghijklmnopqrst"[10:2:-1]
```




    'kjihgfed'




```python
"abcdefghijklmnopqrst"[10::-1]
```




    'kjihgfedcba'




```python
"abcdefghijklmnopqrst"[:3:-1]
```




    'tsrqponmlkjihgfe'




```python
"abcdefghijklmnopqrst"[::-1]
```




    'tsrqponmlkjihgfedcba'




```python
"alekos"[::-1]
```




    'sokela'




```python
"alekos"[::]
```




    'alekos'




```python
# python slicing 
```


```python
"abcdefghijklmnopqrst"[ 10  :  2  : -1  ]
```




    'kjihgfed'




```python
"abcdefghijklmnopqrst"[ 2  :  10  : +1  ]
```




    'cdefghij'




```python
"abcdefghijklmnopqrst"[ -2  :  2  : -1  ]
```




    'srqponmlkjihgfed'




```python
"abcdefghijklmnopqrst"[ -2  :  2  : -1  ]
```




    ''




```python
"abcdefghijklmnopqrst"[::-1]
```




    'tsrqponmlkjihgfedcba'




```python
"ACGTGGTGCCCGGG"[::-1]
```




    'GGGCCCGTGGTGCA'




```python
"fasdfasdfasdfasdfasdf".count('a')
```




    5




```python
"fasdfasdfasdfasdfasdf".count('f')
```




    6




```python
len("fasdfasdfasdfasdfasdf")
```




    21




```python
"    fasdfasdfasdfasdf      ".strip()
```




    'fasdfasdfasdfasdf'




```python
"++fasdfasdfasdfasdf++".strip('+')
```




    'fasdfasdfasdfasdf'




```python
"xaralampos".replace('a', 'b')
```




    'xbrblbmpos'




```python
"xaralampos".replace('a', 'b').count('b')
```




    3




```python
"xaralampos".replace('a', 'b').replace('x', 'l')
```




    'lbrblbmpos'




```python
"xaralampos".replace('ar', '')
```




    'xalampos'




```python
"xaralampos".replace('ar', '--')
```




    'x--alampos'




```python
"xaralampos".replace('ar', '--').replace('pos', '+++')
```




    'x--alam+++'




```python
len("asdfasdfasdfasdfasdf")
```




    20




```python
len('')
```




    0




```python
len('                      ')
```




    22




```python
len(' ')
```




    1




```python
len('')
```




    0




```python
type(45)
```




    int




```python
type(45.0)
```




    float




```python
type('mitsos')
```




    str




```python
int(45.0)
```




    45




```python
int(45.1)
```




    45




```python
float(45)
```




    45.0




```python
int("    45       ")
```




    45




```python
float("   45.3   ")
```




    45.3




```python
str(45)
```




    '45'




```python
str(45.3)
```




    '45.3'




```python
5+6
```




    11




```python
"alekos" + "mitsops"
```




    'alekosmitsops'




```python
float("mitsos")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-130-0b88b66811b2> in <module>()
    ----> 1 float("mitsos")
    

    ValueError: could not convert string to float: 'mitsos'



```python
str(66666)
```




    '66666'




```python
False + False
```




    0




```python

```


```python
True + True
```




    2




```python
True + True
```




    2




```python
True and True
```




    True




```python
True and False
```




    False




```python
False and True
```




    False




```python
False and False
```




    False




```python
0 and 1
```




    0




```python
5 + 3
```




    8




```python
5 < 3
```




    False




```python
3 < 5
```




    True




```python
3 < 3
```




    False




```python
3 <= 3
```




    True




```python
3 > 5
```




    False




```python
3 >= 3
```




    True




```python
3 == 3
```




    True




```python
3== 4
```




    False




```python
"mitsos" == "mitsos"
```




    True




```python
"mitsos" == "Mitsos"
```




    False




```python
"5" == 5
```




    False




```python
5 == 5
```




    True




```python
"5" == "5"
```




    True




```python
5.0 == 5
```




    True




```python
5 != 3
```




    True




```python
5 != 5
```




    False




```python
5 == 5
```




    True




```python
5 == 3
```




    False




```python
"asdasdasdasd".count('a')
```




    4




```python
"asdasdasdasd".count('q') == 0
```




    True




```python
 True  and True
```




    True




```python
False and True
```




    False




```python
True and False
```




    False




```python
False and False
```




    False




```python
3<5 and 5<3
```




    False




```python
"mitsos" == "mitsos" and 3==5-2
```




    True




```python
("mitsos" == "mitsos") and (3==5-2)
```




    True




```python
10+6/2
```




    13.0




```python
10 + (6/2)
```




    13.0




```python
1/1
```




    1.0




```python
10 + (6*2)
```




    22




```python
True and False
```




    False




```python
True or False
```




    True




```python
True or True  
```




    True




```python
True or False
```




    True




```python
False or True
```




    True




```python
False or False 
```




    False



```
or --->   ή
and -->   κα
```

καλός καιρός ΚΑΙ ΔΕΝ εχω δουλειά


καλός καιρός Ή ΔΕΝ εχω δουλειά




```python
+4
```




    4




```python
-4
```




    -4




```python
not False
```




    True




```python
not True
```




    False




```python
(True and True) or (False and True)
```




    True




```python
(5+3) - (4*2)
```




    0




```python
not (False or True)
```




    False




```python
4 + (True or False)
```




    5




```python
0 and True
```




    0




```python
0.0000000000000000000001 and True
```




    True




```python
type(3)
```




    int




```python
type(True)
```




    bool




```python
bool(0)
```




    False




```python
bool(1)
```




    True




```python
bool(0.000000000001)
```




    True




```python
bool(-0.0000000000001)
```




    True




```python
bool('mitsos')
```




    True




```python
bool('')
```




    False




```python
bool(' ')
```




    True




```python
int(45.5)
```




    45




```python
int("45")
```




    45




```python
type(4+5j)
```




    complex




```python
complex(5)
```




    (5+0j)




```python
"                       "
```




    '                       '




```python
3+5
```




    8




```python
3 + 5
```




    8




```python

```
